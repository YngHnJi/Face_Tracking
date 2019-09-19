# Login system, based on user data
# it uses different face data to train model for Face ID
# when it return 1, which means login successfully and
# code goes to "Train model"

from os import listdir, path

def user_login_system():
    # load all user infos to check duplicates
    # user data stored in this computer, to prevent from
    login_flag = 0
    user_data = []

    user_info = listdir("user_info/")
    for user in user_info:
        name, _ = path.splitext(user)
        user_data.append(name)

    while(login_flag == 0):
        print("Welcome...")
        welcome = input("Do you have an acount? y/n: ")
        if welcome == "n":
            while True:
                username = input("Enter a username:")
                if(username in user_data):
                    print("You can't use this user name")
                    break
                password = input("Enter a password:")
                password1 = input("Confirm password:")
                if password == password1:
                    file = open("user_info/" + username + ".txt", "w")
                    file.write(username + ":" + password)
                    file.close()
                    welcome = "y"
                    break
                print("Passwords do NOT match!")

        if welcome == "y":
            while True:
                login1 = input("Login:")
                login2 = input("Password:")
                file = open("user_info/" + login1 + ".txt", "r")
                data = file.readline()
                file.close()
                if data == login1 + ":" + login2:
                    login_flag = 1
                    print("Welcome")
                    #break
                    return True, login1
                print("Incorrect username or password.")

if __name__ == "__main__":
    a, username = user_login_system()
    print(username)