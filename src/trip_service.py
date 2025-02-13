import time
from datetime import datetime
import sys
import os
import logging
import random
import numpy as np
from src.billing import calculate_cost, apply_vat, set_dynamic_rates

# Log configuration
logging.basicConfig(
    filename='taximeter.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def generate_demand_factor():
    """Genera un factor de demanda aleatorio con distribución normal"""
    mean = 1.0  # Media del factor de demanda (por defecto sin demanda especial)
    std_dev = 0.3  # Desviación estándar para la variabilidad del factor

    # Genera el factor con una distribución normal
    demand_factor = np.random.normal(mean, std_dev)
    # Asegurarse de que el factor esté en un rango razonable (por ejemplo entre 0.5 y 2.5)
    return max(0.5, min(demand_factor, 2.5))

def start_trip():
    """
    Simulate a taxi trip and calculate the cost.
    This function now includes the loop for repeating trips.
    """
    while True:
        # Preguntar si el usuario quiere el factor de demanda automático o manual
        choice = input("Do you want to set demand factor automatically (A) or manually (M)? ").strip().lower()

        if choice == 'a':  # Si elige automático, generamos un valor aleatorio
            demand_factor = generate_demand_factor()
            print(f"Demand factor set by algorithm: {demand_factor:.2f}")
            logging.info("Getting demand factor by algotihm.")
        elif choice == 'm':  # Si elige manual, pide al usuario que ingrese el valor
            demand_factor = float(input("Please enter the demand factor (e.g., 1.0 for normal): ").strip())
            print(f"Demand factor manually set to: {demand_factor:.2f}")
            logging.info("Manually set demand factor: {demand_factor:.2f}.")
        else:
            print("Invalid choice. Setting demand factor to default value (1.0).")
            logging.info("Invalid choice. Setting demand factor to default value (1.0).")
            demand_factor = 1.0

        # Establecer las tarifas dinámicas según el factor de demanda
        set_dynamic_rates(demand_factor)

        # Inicialización de variables para cada nuevo viaje
        time_stopped = 0
        time_moving = 0
        taxi_moving = False  # Inicialmente, el taxi está detenido
        trip_active = True
        
        while trip_active:
            print("Started trip... Press Ctrl+C to exit at any time.")
            logging.info("Trip started.")

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
                    logging.info("Taxi is moving.")                    
                else:
                    print("Taxi is now stopped...")
                    logging.info("Taxi stopped.")

            # Ask if the user wants to end the trip
            if not taxi_moving:
                end_input = input("Do you want to end the trip? (y/n): ").strip().lower()
                if end_input == 'y':                    
                    trip_active = False
                    print("Calculating trip cost...")
                    total_cost = calculate_cost(time_stopped, time_moving)
                    total_cost_with_vat = apply_vat(total_cost)
                    logging.info("Calculated trip cost.")
                    print(f"Trip ended. Total cost (without VAT): {total_cost:.2f} €")
                    print(f"Total cost (with 21% VAT): {total_cost_with_vat:.2f} €")
                    logging.info(f"Trip ended. Total cost (without VAT): {total_cost:.2f} €")
                    logging.info(f"Total cost (with 21% VAT): {total_cost_with_vat:.2f} €")
                    
                    # Guardar el historial del viaje
                    with open('trip_history.txt', 'a') as f:
                        f.write(f"{datetime.now()} | Time stopped: {time_stopped:.2f}s | Time moving: {time_moving:.2f}s | Total cost: {total_cost_with_vat:.2f}€\n")

                else:
                    print("Continuing the trip...")
                    logging.info("Continuing the trip.")
            else:
                print("Continuing the trip...")
                logging.info("Continuing the trip.")

        # Ask if user wants to start another trip
        user_input = input("Do you want to start another trip? (y/n): ").strip().lower()
        if user_input != 'y':
            print("Thank you for using the Taximeter App. Goodbye!")
            logging.info("App closed.")
            break
