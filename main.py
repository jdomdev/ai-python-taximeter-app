from src.trip_service import start_trip

def main():
    print("Welcome to the Taximeter App!")
    print("This app calculates the cost of your trip based on time stopped and time in motion.")
    print("Press Ctrl+C to exit at any time.\n")

    # Call the function that starts the trip
    start_trip()

if __name__ == "__main__":
    main()
