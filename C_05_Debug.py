import random

def instructions():
    print('''

**** Instructions ****

To begin, depending on the amount of rounds you pick for the quiz, 
you will need to answer the questions you are given. (Like any normal quiz of course).

You will need to type the correct number to answer the equation you are asked.

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

def int_check(question, low=None, exit_code=None):

    error = "Please enter a valid integer."

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:

            response = int(response)

            # check int not too low...
            if low is not None and response < low:
                print(error)

        except ValueError:
            print(error)


# Main code starts here

# Initialize game variables
mode = "regular"
rounds_played = 0
user_wrong = 0
user_right = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("➕➖✖️ Welcome to the fun and amazing Math Quiz!!! ➕➖✖️")
print()

# Ask user if they want the instructions
want_instructions = yes_no("Would you like to read the instructions? ")

# checks users enter yes (y) or no (n) for instructions
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")

# initialize number of rounds for infinite mode
if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# game loop starts here

while rounds_played < num_rounds:

    # Headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🎲🎲🎲 Round {rounds_played + 1} of {num_rounds} 🎲🎲🎲"

    print(rounds_heading)

    # Pick 2 random numbers for the equation
    roll_one = random.randint(0, 12)
    roll_two = random.randint(0, 12)

    # pick a random symbol for the equation
    symbol_list = ['+', '-', '*',]
    symbol = random.choice(symbol_list)
    # this line not needed. [symbol = str(symbol)]

    # Solve equation and ask user for their answer
    equation = f"{roll_one} {symbol} {roll_two}"
    question_ans = eval(equation)
    print(f"Question {rounds_played+1}: {roll_one} {symbol} {roll_two}")
    user_ans = int_check("What is your answer? ", exit_code="xxx")

    # check if user gets the question right
    if user_ans == question_ans:
        feedback = f"Correct! You guessed {user_ans}, and the correct answer is also {question_ans}!"
        user_right += 1
    # check if user gets the question wrong
    elif user_ans != question_ans:
        feedback = f"Incorrect! You guessed {user_ans}, but the correct answer was {question_ans}!"
        user_wrong += 1

    print(feedback)
    print()


    # Game History and Stats

    # generate round results and add it to the game history list
    history_feedback = f"Round {rounds_played + 1}: {feedback}"

    game_history.append(history_feedback)

    # increase number of rounds played
    rounds_played += 1

    # if users in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# check users have played at least one round
# before calculating stats.
if rounds_played > 0:
    # calculate stats
    rounds_won = rounds_played - user_wrong
    percent_won = user_right / rounds_played * 100
    percent_lost = user_wrong / rounds_played * 100

    # Output Game Stats
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"😎 Percentage of games won: {percent_won:.2f}% \t "
          f"😭 Percentage of games lost: {percent_lost:.2f}% \t ")

    # ask user if they want to see game history
    see_history = yes_no("Do you want to see the game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)
            print()

    # Say goodbye
    print("Thanks for playing!")




