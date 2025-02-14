import time
from datetime import datetime
import sys
import os
import logging
import random
import numpy as np
from src.billing import calculate_cost, apply_vat, set_dynamic_rates

# Configure logging to store events in a file
logging.basicConfig(
    filename='taximeter.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ensure the script's directory is included in the system path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def demand_factor_algorithm():
    """
    Generates a random demand factor using a normal distribution.
    Ensures the value is within a reasonable range (0.5 to 2.5).
    """
    mean = 1.0  # Default demand factor (no special demand)
    std_dev = 0.3  # Standard deviation for variability
    
    # Generate the demand factor using a normal distribution
    demand_factor = np.random.normal(mean, std_dev)
    
    # Ensure the factor stays within the range of 0.5 to 2.5
    return max(0.5, min(demand_factor, 2.5))

def automatic_or_manual_factor():
    """
    Asks the user whether to set the demand factor automatically or manually.
    Returns the chosen demand factor.
    """
    choice = input("Do you want to set demand factor automatically (A) or manually (M)? \n").strip().lower()

    if choice == 'a':
        # Generate a random demand factor
        demand_factor = demand_factor_algorithm()
        print(f"Demand factor set by algorithm: {demand_factor:.2f}\n")
        logging.info("Getting demand factor by algorithm.")
    elif choice == 'm':
        # Ask the user for manual input
        demand_factor = float(input("Please enter the demand factor (e.g., 1.0 for normal): ").strip())
        print(f"Demand factor manually set to: {demand_factor:.2f}\n")
        logging.info(f"Manually set demand factor: {demand_factor:.2f}.")
    else:
        # Default to 1.0 if the input is invalid
        print("Invalid choice. Setting demand factor to default value (1.0).\n")
        logging.info("Invalid choice. Setting demand factor to default value (1.0).")
        demand_factor = 1.0
    return demand_factor

def end_trip(taxi_moving, time_stopped, time_moving):
    """
    Handles the process of ending a trip.
    If the taxi is stopped, it asks the user whether to end the trip.
    Calculates the total cost and stores trip details.
    """
    if not taxi_moving:
        end_input = input("Do you want to end the trip? (y/n): ").strip().lower()
        if end_input == 'y':                    
            print("Calculating trip cost...")
            total_cost = calculate_cost(time_stopped, time_moving)
            total_cost_with_vat = apply_vat(total_cost)
            logging.info("Calculated trip cost.")
            print(f"Trip ended. Total cost (without VAT): {total_cost:.2f} €")
            print(f"Total cost (with 21% VAT): {total_cost_with_vat:.2f} €\n")
            logging.info(f"Trip ended. Total cost (without VAT): {total_cost:.2f} €")
            logging.info(f"Trip ended. Total cost (with 21% VAT): {total_cost_with_vat:.2f} €")
            # Save trip history
            with open('trip_history.txt', 'a') as f:
                f.write(f"{datetime.now()} | Time stopped: {time_stopped:.2f}s | Time moving: {time_moving:.2f}s | Total cost: {total_cost_with_vat:.2f}€\n")
            return False  # The trip has ended
        else:
            print("Continuing the trip...\n")
            logging.info("Continuing the trip.")
            return True  # The trip continues
    else:
        print("Continuing the trip...\n")
        logging.info("Continuing the trip.")  
        return True  # The trip continues

def another_trip():
    """
    Asks the user whether they want to start another trip.
    Returns True if another trip should be started, otherwise False.
    """
    user_input = input("Do you want to start another trip? (y/n): \n").strip().lower()
    if user_input == 'y':
        return True  # User wants another trip
    else:
        print("Thank you for using the Taximeter App. Goodbye!")
        logging.info("App closed.")
        return False  # User does not want another trip

def start_trip():
    """
    Simulates a taxi trip and calculates the cost.
    Includes a loop for repeating trips.
    """
    while True:
        # Ask the user for the demand factor
        demand_factor = automatic_or_manual_factor()

        # Set dynamic pricing based on the demand factor
        set_dynamic_rates(demand_factor)

        # Initialize trip variables
        time_stopped = 0
        time_moving = 0
        taxi_moving = False  # Initially, the taxi is stopped
        trip_active = True
        print("Started trip... Press Ctrl+C to exit at any time.\n")
        logging.info("Trip started.")
        
        while trip_active:
            # Start the timer
            start_time = datetime.now()

            # Ask if the taxi should move or stop
            if taxi_moving:
                move_input = input("Do you want to stop the taxi? (y/n): ").strip().lower()
            else:
                move_input = input("Do you want to start moving the taxi? (y/n): ").strip().lower()

            # Calculate elapsed time
            end_time = datetime.now()
            elapsed_time = (end_time - start_time).total_seconds()

            # Update time based on taxi state
            if taxi_moving:
                time_moving += elapsed_time
            else:
                time_stopped += elapsed_time

            # Toggle taxi movement based on user input
            if move_input == 'y':
                taxi_moving = not taxi_moving  # Toggle state
                if taxi_moving:
                    print("Taxi is now moving...\n")
                    logging.info("Taxi is moving.")                    
                else:
                    print("Taxi is now stopped...\n")
                    logging.info("Taxi stopped.")
            
            # Update trip status based on user input
            trip_active = end_trip(taxi_moving, time_stopped, time_moving)
        
        # Ask if the user wants another trip
        if not another_trip():
            break
