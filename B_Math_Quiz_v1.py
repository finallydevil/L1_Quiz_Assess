import random

def instructions():
    print('''

**** Instructions ****

To begin, depending on the amount of rounds you pick for the quiz, 
you will need to answer the questions you are given. (Like any normal quiz of course).

You will need to choose either A, B, C, or D. as this quiz is a multi choice quiz.

Your goal is to try and get as many questions right. 

Good Luck!!!!!!!!!!!!!

    ''')

def yes_no(question):
    while True:
        response = input(question).lower()

        # check response,
        # check if user says yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter 'yes' or 'no'")

def int_check(question, low=None, high=None, exit_code=None):

    # if any int is allowed
    if low is None and high is None:
        error = "Please enter a valid integer."

    # if the number needs to be more than an
    # integer
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"greater than or equal to {low}.")

    # if number needs to be between low & high
    else:
        error = (f"Please enter an integer that is "
                 f"between {low} and {high} (inclusive).")

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # check int not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return
            else:
                return response

        except ValueError:
            print(error)

def rand_question(equation, question_ans):


    # Pick 2 random numbers for the equation
    roll_one = random.randint(0, 12)
    roll_two = random.randint(0, 12)

    # pick a random symbol for the equation
    symbol_list = ['+', '-', '*',]
    symbol = random.choice(symbol_list)
    symbol = str(symbol)

    equation = f"Question: {roll_one} {symbol} {roll_two}"
    question_ans = eval(equation)
    return equation


# Main code starts here

# Initialize game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("Welcome to the fun and amazing Math Quiz!!!")
print()

want_instructions = yes_no("Would you like to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# game loop starts here

while rounds_played < num_rounds:
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🎲🎲🎲 Round {rounds_played + 1} of {num_rounds} 🎲🎲🎲"



