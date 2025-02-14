import getpass
import logging

class Authentication:
    USERS = {"admin": "1234"}  # User credentials stored in a dictionary

    @staticmethod
    def login():
        """Requests user credentials and validates access."""
        user = input("Username: ")
        password = getpass.getpass("Password: ")

        if Authentication.USERS.get(user) == password:
            logging.info(f"User {user} logged in successfully.")
            print("Access granted!")
            return True
        else:
            logging.warning(f"Failed login attempt for user {user}.")
            print("Invalid credentials. Exiting...")
            return False
