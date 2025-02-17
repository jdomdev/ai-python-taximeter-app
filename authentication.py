import logging

class Authentication:
    USERS = {"admin": "1234"}  # User credentials stored in a dictionary

    @staticmethod
    def authenticate(username, password):
        """
        Authenticates the user.
        :param username: The username.
        :param password: The password.
        :return: True if authentication is successful, False otherwise.
        """
        if Authentication.USERS.get(username) == password:
            logging.info(f"User {username} logged in successfully.")
            return True
        else:
            logging.warning(f"Failed login attempt for user {username}.")
            return False