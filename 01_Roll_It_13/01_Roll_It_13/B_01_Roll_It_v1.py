
# function start
def yes_no(question):
    """Checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:
        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes / no")


def instructions():
    """prints instructions"""

    print("""
*** Instructions ***

roll the dice and try to win!
    """)


def int_check():
    """checks users enter an integer more than / equal to 13"""
    error = "please enter an integer more than / equal to 13."
    while True:
        try:
            response = int(input("what is the game goal"))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine

# ask the user if they want instructions (check if they say yes / no)
want_instructions = yes_no("do you want to see the instructions?")
print(f"you chose {want_instructions}")
# Display the instructions if user wants to see them
if want_instructions == "yes":
    instructions()

    print()
game_goal = int_check()
print(game_goal)

