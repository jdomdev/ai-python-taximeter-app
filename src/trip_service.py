import time
from datetime import datetime
from src.billing import calculate_cost, apply_vat
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def start_trip():
    """
    Simulate a taxi trip and calculate the cost.
    This function now includes the loop for repeating trips.
    """
    while True:
        # Inicialización de variables para cada nuevo viaje
        time_stopped = 0
        time_moving = 0
        taxi_moving = False  # Inicialmente, el taxi está detenido
        trip_active = True

        print("Trip started. Press Ctrl+C to exit at any time.")

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

            # Update taxi state based on user input
            if move_input == 'y':
                taxi_moving = not taxi_moving  # Toggle taxi state
                if taxi_moving:
                    print("Taxi is now moving...")
                else:
                    print("Taxi is now stopped...")

            # Ask if the user wants to end the trip
            if not taxi_moving:
                end_input = input("Do you want to end the trip? (y/n): ").strip().lower()
                if end_input == 'y':
                    trip_active = False
                    print("Calculating trip cost...")
                    total_cost = calculate_cost(time_stopped, time_moving)
                    total_cost_with_vat = apply_vat(total_cost)

                    print("\nTrip Summary:")
                    print(f"Time stopped: {time_stopped:.2f} seconds")
                    print(f"Time moving: {time_moving:.2f} seconds")
                    print(f"Total cost (without VAT): {total_cost:.2f} €")
                    print(f"Total cost (with 21% VAT): {total_cost_with_vat:.2f} €")
                else:
                    print("Continuing the trip...")
            else:
                print("Continuing the trip...")

        # Ask if user wants to start another trip
        user_input = input("Do you want to start another trip? (y/n): ").strip().lower()
        if user_input != 'y':
            print("Thank you for using the Taximeter App. Goodbye!")
            break
