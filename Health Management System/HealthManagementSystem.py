# Exercise 5 - Health Management System
# Objectives : Make function for diet & fitness workout logging and retrieving to/from individual files with timestamp
# Overview: For 3 clients viz., Harry, Rohan and Hammad; 3 options will be available for both logging and retrieving
# data, function to write to log by having their input data with time and to retrieve from their individual files
# Given date time function to use:

# -----------------------Header----------------------- #

title = "Exercise 5 - Health Management System"
subtitle = "[Note: Log & retrieve client's food and workout record]"
underline = int(len(subtitle)) * "-"
print("\n{}\n{}\n{}\n".format(title, underline, subtitle))

# -----------------------Variables----------------------- #

welcome_address = ["Hi,", "Hello,", "Hello there,", "Hey,"]

# -user related variables should be imported\exported from a file
# -e.g., no_of_users, user_names and user_options
no_of_users = 3
user_database = {
    "1": {
        "name": "Harry",
        "file_diet": "HMS_Harry_DietRecord.txt",
        "file_workout": "HMS_Harry_WorkoutRecord.txt"
    },
    "2": {
        "name": "Rohan",
        "file_diet": "HMS_Rohan_DietRecord.txt",
        "file_workout": "HMS_Rohan_WorkoutRecord.txt"
    },
    "3": {
        "name": "Hammad",
        "file_diet": "HMS_Hammad_DietRecord.txt",
        "file_workout": "HMS_Hammad_WorkoutRecord.txt"
    }
}

user_options = ["1", "2", "3"]
user_actions = ["1", "2"]

user_typed = ""


# -----------------------Functions----------------------- #


def get_date():
    """Prints/Returns current date and time"""
    import datetime
    return datetime.datetime.now()


def welcome_task():
    """Handles welcome tasks for user to choose an option for"""
    print("\nChoose your name to continue with HMS\n Type,")
    for user_id, user_info in user_database.items():
        print("  ", user_id, "for ...", user_info["name"].upper())

    global user_typed
    user_typed = input("\nWhat's it? ")

    if user_typed not in user_options:
        print("\nINVALID: You typed a wrong option! Try again with a right one.")
        welcome_task()


def read_write_line(file_name, arg):
    """
    In-program function to write user input line to a input file

    :param file_name: Input log file name
    :param arg: Argument specification for file operation
    :return: Append user input as a single line to input file
    """
    try:
        with open(file_name, arg) as file:
            if arg is "a+":
                print("[i] Write and press enter to save.\n")
                line = input()
                print("\nWAIT, saving changes to the file ...")
                file.write("{} - {}\n".format(get_date(), line))
                print("OK, file saved!")

                again = input("\nDo you want to write more line(s)? If yes, press 1 or enter to exit: ")
                if again == "1":
                    read_write_line(file_name, arg)
                else:
                    print("SURE, exiting HMS ...")
            else:
                print("\nWAIT, retrieving saved data from file ...")
                file.seek(0)
                print("\nDONE, file retrieved!\n==== FILE START: {} ----------------------------------\n".format(file_name))
                print(file.read())
                print("==== FILE END: {} ------------------------------------".format(file_name))
    except Exception as exp:
        print("\n{}\nSORRY, you didn't log any data yet!\nDo log your data first and then try again.".format(exp))


def user_action(user_id):
    """Performs main user actions"""
    print("\nWelcome {0}! It's now {1}".format(user_id["name"], get_date()))
    print("What do you want to perform now?\n Type,")
    print("   1 for ... Logging\n   2 for ... Retrieving")

    user_choose = input("\nWhat's it? ")

    if user_choose in user_actions:
        if user_choose == "1":
            def user_log():
                print("   1 for ... Dietary Logging\n   2 for ... Workout Logging")
                user_choose_log = input("\nWhat's it? ")

                if user_choose_log == "1":
                    print("\n{}, log your dietary intake. Submit one line at time.\nGive what you actually ate with "
                          "approx amount, time will automatically be added.".format(user_id["name"]))
                    read_write_line(user_id["file_diet"], "a+")
                elif user_choose_log == "2":
                    print("\n{}, log your workout activities. Submit one line at time.\nGive what you actually did "
                          "with approx duration, time will automatically be added.".format(user_id["name"]))
                    read_write_line(user_id["file_workout"], "a+")
                else:
                    print("\nINVALID: You typed a wrong option! Try again with a right one.")
                    user_log()
            user_log()
        else:
            def user_rtv():
                print("   1 for ... Dietary Retrieving\n   2 for ... Workout Retrieving\n")
                user_choose_rtv = input("\nWhat's it? ")

                if user_choose_rtv == "1":
                    print("\n{}, retrieve your dietary intake data with time when you logged.".format(user_id["name"]))
                    read_write_line(user_id["file_diet"], "rt")
                elif user_choose_rtv == "2":
                    print("\n{}, retrieve your timely workout activity related data".format(user_id["name"]))
                    read_write_line(user_id["file_workout"], "rt")
                else:
                    print("\nINVALID: You typed a wrong option! Try again with a right one.")
                    user_rtv()
            user_rtv()
    else:
        print("\nINVALID: You typed a wrong option! Try again with a right one.")
        user_action(user_database[user_typed])


# -----------------------Main Program----------------------- #

print(welcome_address.__getitem__(2), "good to see you here!\nWelcome you to the HEALTH MANAGEMENT SYSTEM!")
print("\nToday is", get_date())

welcome_task()

user_action(user_database[user_typed])

print("\n\nTHANKS, for using our service!\nCome again, write and we'll make a log for you to keep you on "
      "stark towards a healthier life.")
print("[Upcoming Updates: Quit in any step, Reset existing record(s), Date-time re-formation, Line separator for "
      "new date, Item & Quantity/Duration separation, 24h recall calculator]")
