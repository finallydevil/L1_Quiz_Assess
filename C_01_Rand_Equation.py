import random

# Pick 2 random numbers for the equation
roll_one = random.randint(0, 12)
roll_two = random.randint(0, 12)

# pick a random symbol for the equation
symbol_list = ['+', '-', '*', ]
symbol = random.choice(symbol_list)
symbol = str(symbol)

equation = f"{roll_one} {symbol} {roll_two}"
question_ans = eval(equation)

print(equation)
print(question_ans)