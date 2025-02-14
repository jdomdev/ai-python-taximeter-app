from src.trip_service import start_trip
import logging

# Log configuration
logging.basicConfig(
    filename='taximeter.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    print("\nWelcome to the Taximeter App!")
    print("This app calculates the cost of your trip based on time stopped and time in motion.")
    print("Press Ctrl+C to exit at any time.\n")
    logging.info("Aplication started.")

    # Call the function that starts the trip
    start_trip()

if __name__ == "__main__":
    main()
