import tkinter as tk
import logging
from taximeter import Taximeter
from authentication import Authentication

class TaximeterApp:
    def __init__(self, root):
        """
        Initializes the graphical interface.
        :param root: The main Tkinter window.
        """
        self.taximeter = Taximeter()
        self.root = root
        self.root.title("Taximeter")

        self.label = tk.Label(root, text="Taxi Stopped", font=("Arial", 14))
        self.label.pack(pady=10)

        self.toggle_button = tk.Button(root, text="Start/Stop", command=self.toggle)
        self.toggle_button.pack(pady=5)

        self.calculate_button = tk.Button(root, text="Calculate Cost", command=self.calculate_cost)
        self.calculate_button.pack(pady=5)

        self.cost_label = tk.Label(root, text="", font=("Arial", 12))
        self.cost_label.pack(pady=10)

        logging.info("GUI initialized.")

    def toggle(self):
        """Toggles taxi movement and updates GUI."""
        self.taximeter.toggle_movement()
        self.label.config(text="Taxi Moving" if self.taximeter.taxi_moving else "Taxi Stopped")

    def calculate_cost(self):
        """Calculates trip cost and displays result in GUI."""
        cost = self.taximeter.calculate_trip_cost()
        self.cost_label.config(text=f"Total cost: {cost:.2f} €")

if __name__ == "__main__":
    if Authentication.login():
        root = tk.Tk()
        app = TaximeterApp(root)
        root.mainloop()
