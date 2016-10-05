"""Administrator role and privileges of the users related classes."""

from userm import User

class Privileges():
    """Trying to model real-world privileges."""

    def __init__(self):
        """Initialize attributes of the Privileges class."""
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
            ]

    def show_privileges(self):
        """Method that shows the privileges of the user."""
        print("The user has next privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    """Trying to model real-world administrators of some website."""

    def __init__(
            self,
            first_name,
            last_name,
            username,
            age,
            location
        ):
        """
        Initializing attributes of the parent class User.
        Adding attributes specific to the Class Admin.
        """
        super().__init__(
            first_name,
            last_name,
            username,
            age,
            location
            )
        self.privileges = Privileges()