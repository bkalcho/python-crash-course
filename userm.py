"""User class module, which models real-world user"""

class User():
    """Trying to model real-world users of the some website."""

    def __init__(
            self,
            first_name,
            last_name,
            username,
            age,
            location):
        """Initializing attributes of the class Users."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Method that prints summary of the user information."""
        print("We have stored next information about user " +
                self.first_name.title() + " " + self.last_name.title() +
                ":")
        print("- Username: " + self.username)
        print("- Age: " + str(self.age))
        print("- Location: " + self.location.title())

    def greet_user(self):
        """Method that print personalized greeting to the user."""
        print("Hello " + self.first_name.title() + " " +
            self.last_name.title() + ", welcome back!")

    def increment_login_attempts(self):
        """Increment login attempts for 1."""
        self.login_attempts += 1

    def reste_login_attempts(self):
        """Method that resets value of login attempts to 0."""
        self.login_attempts = 0