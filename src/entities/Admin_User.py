from entities.Movie import Movie
from repositories.Admin_User_Repository import Admin_User_Repository
from repositories.Movie_Repository import Movie_Repository
from services.Movie_Service import Movie_Service


class Admin_user():


    def __init__(self, username, password):
        self.username = username
        self.password = password


    def create_new_admin_user():
        """ Creating a new admin user. Need to have a unique username that is at least
        3 characters long. Note: this function does not inform new admin user.
        The creator has to do it manually.
        """

        username = input("Choose admin username (min. 3 characters long:) ")

        username_is_unique = Admin_user.check_if_username_is_available(username)
        username_is_long_enough = Admin_user.check_username_length(username_is_unique)
        username = username_is_long_enough

        password = input("Choose password (min. 3 characters long): ")
        password_is_long_enough = Admin_user.check_password_lenght(password)
        password = password_is_long_enough

        Admin_User_Repository.admin_users[username] = password
        Admin_User_Repository.save_new_admin_user_to_file(username, password)

        print("\nNew admin user created.")
        print("Remember to send user account cresentials to the new admin. \n")


    def admin_log_in():
        """ Log in for admin users. Check if username and password match.
        """

        admin_username = input("What is your admin username? ")

        # Check is username exists
        username_exists = False
        while True:

            if username_exists:
                username_exists = True
                break

            if admin_username not in Admin_User_Repository.admin_users:
                print("I don't recognize this username. ")
                admin_username = input("Please give correct admin username: ")

            if admin_username in Admin_User_Repository.admin_users:
                break

        admin_password = input("What is your password? ")

        if Admin_User_Repository.admin_users[admin_username] != admin_password:
            password_is_correct = False

            while True:
                if password_is_correct:
                    break

                print("Incorrect password. Please try again. \n")
                admin_password = input("Password: ")

                if Admin_User_Repository.admin_users[admin_username] == admin_password:
                    password_is_correct = True

        print(f"Welcome, admin {admin_username}!")
        print("")
        Admin_user.admin_tools()


    def admin_tools():
        """Tools menu for admin level users. Admin can create new admin user, 
        check voting status and handle movie related lists and files.
        """

        while True:

            print("Choose function:")
            print("  [P]rint current voting list ")
            print("  [C]lear voting list ")
            print("  [R]ead suggestions for next weeks movie voting ")
            print("  [S]et up a new votings list ")
            print("  [K] Check voting status ")
            print("  [M]ake new admin user account ")
            print("  [E]xit admin tools \n")
            choice = input("My choice: ")

            if choice in ("E", "e"):
                break
            if choice in("P", "p"):
                Movie.print_voting_list_for_admin()
            elif choice in ("C", "c"):
                Movie_Repository.empty_voting_list()
            elif choice in ("R", "r"):
                Movie.print_movie_suggestion_list()
            elif choice in ("S", "s"):
                Movie.set_voting_list()
            elif choice in ("K", "k"):
                Movie_Service.check_voting_list_status()
            elif choice in ("M", "m"):
                Admin_user.create_new_admin_user()
            else:
                print("Please choose from the list. \n")


    def check_if_username_is_available( username):
        """Check if suggested username is already in use among Admin Users.
        """

        username_is_unique = False

        while True:

            if username_is_unique:
                break

            if username in Admin_User_Repository.admin_users:
                print("This username is already taken.")
                username = input("Please choose unique username: ")
                continue
            username_is_unique = True

        return username


    def check_username_length(username):
        while True:
            if len(username) >= 3:
                return username
            print("You chose too short username. It should be at least 3 characters long.")
            username = input("Please choose longer username: ")


    def check_password_lenght(password):
        while True:
            if len(password) >= 3:
                return password
            print("You chose too short password. It should be at least 3 characters long.")
            password = input("Please choose longer username: ")
