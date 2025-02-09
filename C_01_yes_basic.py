
print("hello")

while True:
    want_instructions = input("do you want to see the instructions?").lower()

    # check the user says yes / no
    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("you said no")
        break
    else:
        print("please answer yes / no")
        continue
print("done :]")
print("hello")


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


# Main routine

want_instructions = yes_no("do you want to see the instructions?")
print(f"you chose {want_instructions}")
# Display the instructions if user wants to see them
if want_instructions == "yes":
    instructions()

    print()
print("program continues")

error = "please enter an integer more than / equal to 13."
while True:
    try:
        game_goal = int(input("what is the game goal"))

        if game_goal < 13:
            print(error)
        else:
            print("game goal: {game_goal}")
            break

    except ValueError:
        print(error)
