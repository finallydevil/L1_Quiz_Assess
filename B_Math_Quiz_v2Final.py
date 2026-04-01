import random

# Yes or No checker
def yes_no(question):
    """Checks that the users response to a question is yes / no (y/n), returns 'yes' or 'no' """

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

# Instructions
def instructions():
    """Prints the instructions if user asks for it"""

    print('''

**** Instructions ****

To begin, depending on the amount of rounds you pick for the quiz, 
you will need to answer the questions you are given. (Like any normal quiz of course).

You will need to type the correct number to answer the equation you are asked.

Your goal is to try and get as many questions right. 

Good Luck!!!!!!!!!!!!!

    ''')

# Integer checker
def int_check(question, low=None, exit_code="xxx"):
    """Checks that users enter an integer, makes sure they enter a valid number."""

    # if any int is allowed
    if low is None:
        error = "Please enter a valid integer."

    # if the number needs to be more than an
    # integer
    elif low is not None:
        error = (f"Please enter an integer that is "
                 f"greater than or equal to {low}.")

    # if number needs to be between low & high
    else:
        error = (f"Please enter an integer that is "
                 f"Greater than {low} (inclusive).")

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # check int not too low...
            if low is not None and response < low:
                print(error)

            # if response is valid, return
            else:
                return response

        except ValueError:
            print(error)


# Main code starts here

# Initialize game variables
mode = "regular"
end_game = "no"
feedback = ""
rounds_played = 0
user_wrong = 0
user_right = 0
game_history = []

# Prints the introduction to the quiz.
print("➕➖✖️ Welcome to the fun and amazing Math Quiz!!! ➕➖✖️")
print()

# Ask user if they want the instructions
want_instructions = yes_no("Would you like to read the instructions? ")

# checks users enter yes (y) or no (n) for instructions
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

# Initialize number of rounds for infinite mode
if num_rounds == "":
    mode = "infinite"
    num_rounds = 5


# Game loop starts here

# Create a while loop
while rounds_played < num_rounds:

    # Print the headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🎲🎲🎲 Round {rounds_played + 1} of {num_rounds} 🎲🎲🎲"

    print(rounds_heading)

    # Pick 2 random numbers between one and twelve for the equation
    roll_one = random.randint(0, 12)
    roll_two = random.randint(0, 12)

    # Pick a random symbol between add, subtract, and multiply for the equation
    symbol_list = ['+', '-', '*',]
    symbol = random.choice(symbol_list)
    symbol = str(symbol)

    # Solve equation and ask user for their answer
    equation = f"{roll_one} {symbol} {roll_two}"
    question_ans = eval(equation)
    print(f"Question {rounds_played+1}: {roll_one} {symbol} {roll_two}")
    user_ans = int_check("What is your answer? ", low=None, exit_code="xxx")

    # Check if the user gets the question right, prints feedback and adds 1
    # to the amount of questions the user answered right.
    if user_ans == question_ans:
        feedback = (f"Correct! You guessed {user_ans}!"
                    f"The correct answer is also {question_ans}! 😎")
        user_right += 1
    # Exit code
    if user_ans == "xxx":
        print("Now exiting...")
        break
    # Check if the user gets the question wrong, prints feedback and adds 1
    # to the amount of questions the user answered wrong.
    elif user_ans != question_ans:
        feedback = (f"Incorrect! You guessed {user_ans}..."
                    f"The correct answer was instead {question_ans}. 😢")
        user_wrong += 1

    # Prints feedback
    print(feedback)
    print()

    # Generate round results and add it to the game history list.
    history_feedback = f"Round {rounds_played + 1}: {feedback}"

    game_history.append(history_feedback)

    # Increase number of rounds played by one each time the user plays a round.
    rounds_played += 1

    # If users in infinite mode, increase number of rounds.
    if mode == "infinite":
        num_rounds += 1
        # If users in infinite mode, ask them if they want to quit after answering.
        infinite_ans = yes_no("Would you like to keep playing? ")
        if infinite_ans == "yes":
            continue
        if infinite_ans == "no":
            print("Now exiting infinite mode... ")
            break


# Game history and statistics area

# Check users have played at least one round
# before calculating stats.
if rounds_played > 0:
    # Calculate statistics
    rounds_right = rounds_played - user_wrong
    percent_right = user_right / rounds_played * 100
    percent_wrong = user_wrong / rounds_played * 100

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"😎 Percentage of games won: {percent_right:.2f}% \t "
          f"😭 Percentage of games lost: {percent_wrong:.2f}% \t "
          f"😀 Amount of correct answers: {rounds_right} out of {rounds_played}")

    # Ask user if they want to see game history
    if user_ans != "xxx":
        see_history = yes_no("Do you want to see the game history? ")
        if see_history == "yes":
            for item in game_history:
                print(item)
                print()

# Say goodbye
print("Thanks for playing!")




