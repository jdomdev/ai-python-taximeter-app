import time
import logging
from datetime import datetime
from billing import Billing

# Configure logging for the application
logging.basicConfig(filename="taximeter.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Taximeter:
    def __init__(self, demand_factor=1.0, manual_demand=False):
        """
        Initializes the taximeter.
        :param demand_factor: Demand multiplier (default 1.0).
        :param manual_demand: If True, demand is set manually.
        """
        self.time_stopped = 0
        self.time_moving = 0
        self.taxi_moving = False
        self.billing = Billing(demand_factor)
        self.manual_demand = manual_demand

        logging.info("Taximeter initialized.")

    def toggle_movement(self):
        """Toggles between moving and stopped states."""
        self.taxi_moving = not self.taxi_moving
        state = "moving" if self.taxi_moving else "stopped"
        logging.info(f"Taxi is now {state}.")

    def update_time(self, elapsed_time):
        """Updates time based on the taxi's movement state."""
        if self.taxi_moving:
            self.time_moving += elapsed_time
        else:
            self.time_stopped += elapsed_time

    def calculate_trip_cost(self):
        """Calculates total trip cost."""
        cost = self.billing.calculate_cost(self.time_stopped, self.time_moving)
        logging.info(f"Trip cost calculated: {cost:.2f}€")
        return cost

    def reset(self):
        """Resets the taximeter for a new trip."""
        logging.info(f"Trip ended. Time stopped: {self.time_stopped:.2f}s, Time moving: {self.time_moving:.2f}s")
        self.time_stopped = 0
        self.time_moving = 0
        self.taxi_moving = False
