from core.simulations import start_trip
from core.calculations import calculate_cost, apply_vat

def main():
    print("Welcome to the Taximeter App!")
    print("This app calculates the cost of your trip based on time stopped and time in motion.")
    print("Press Ctrl+C to exit at any time.\n")

    while True:
        start_trip()
        user_input = input("Do you want to start another trip? (y/n): ").strip().lower()
        if user_input != 'y':
            print("Thank you for using the Taximeter App. Goodbye!")
            break

if __name__ == "__main__":
    main()