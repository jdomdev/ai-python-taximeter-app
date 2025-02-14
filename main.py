import logging
from gui import TaximeterApp
import tkinter as tk
from authentication import Authentication

# Configure logging for main events
logging.basicConfig(filename="taximeter.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    logging.info("Application started.")

    if Authentication.login():
        root = tk.Tk()
        app = TaximeterApp(root)
        root.mainloop()

    logging.info("Application closed.")
