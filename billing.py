import logging
import random

class Billing:
    STOP_RATE = 0.02  # Cost per second while stopped
    MOVE_RATE = 0.05  # Cost per second while moving
    VAT_RATE = 0.21  # Value-added tax (VAT)

    def __init__(self, demand_factor=1.0):
        """
        Initializes billing system.
        :param demand_factor: Multiplier for demand pricing.
        """
        self.demand_factor = demand_factor if demand_factor else self.auto_demand_factor()

    def auto_demand_factor(self):
        """Determines automatic demand factor based on random simulation."""
        factor = round(random.uniform(1.0, 2.5), 2)
        logging.info(f"Automatic demand factor set to {factor}")
        return factor

    def calculate_cost(self, time_stopped, time_moving):
        """Calculates the total cost including VAT."""
        base_cost = (time_stopped * self.STOP_RATE) + (time_moving * self.MOVE_RATE)
        total_cost = base_cost * self.demand_factor
        total_cost_with_vat = total_cost * (1 + self.VAT_RATE)
        
        # Log trip details to history file
        with open('trip_history.txt', 'a') as f:
            f.write(f"{time_stopped:.2f}s stopped | {time_moving:.2f}s moving | Cost: {total_cost_with_vat:.2f}€\n")
        
        logging.info(f"Cost calculated: {total_cost_with_vat:.2f}€ (Demand factor: {self.demand_factor})")
        return total_cost_with_vat
