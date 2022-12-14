import sys

class Admin_User_Repository:


    # Dictionary to store all admin users: username as the key and password as the value
    admin_users = {}


    # Check if admin user list is available and if it is, download and save users to a dictionaries
    def check_and_download_admin_userlist():

        admin_userlist_file_exists = False

        while not admin_userlist_file_exists:

            movieapp_admin_userlist = "src/repositories/movieapp_admin_users.txt"

            try:
                # Test if file exists
                with open(movieapp_admin_userlist, encoding="utf-8") as testfile:
                    admin_userlist_file_exists = True

            except OSError:
                print("Error: admin userlist not found.")
                sys.exit()

            # Read file and save admin users to all_users dictionary
            with open(movieapp_admin_userlist, encoding="utf-8") as file:
                for line in file:
                    userdata = line.split(",")
                    username = str.strip(userdata[0])
                    password = str.strip(userdata[1])
                    Admin_User_Repository.admin_users[username] = password

                file.close()

    # Read file and save new user to admin_users dictionary
    def save_new_admin_user_to_file(username, password):
        with open("src/repositories/movieapp_admin_users.txt", "a", encoding="utf-8") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()
            return True
