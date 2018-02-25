from random import randint

WINNING_CASES = [1, 2, 3, 5, 5, 3, 2]
WINNING_CASES_EXPLANATION = ["BIG PRIZE", "Last 6 Digists", "Last 5 Digists", "Last 4 Digits",
                             "Last 3 Digits", "Last 2 Digits", "Amorti"]
NUM_DIGITS = [7, 6, 5, 4, 3, 2, 1]
MAX_DIGITS = NUM_DIGITS[0]


def rand_gen(digit):
    lucky = str(randint(0, 9))
    for i in range(digit - 1):
        lucky += str(randint(0, 9))
    return lucky


lucky_numbers = []
for i in range(MAX_DIGITS):
    lucky_numbers.append([])
    for j in range(WINNING_CASES[i]):
        flag = True
        lucky = rand_gen((NUM_DIGITS[i]))
        if lucky not in lucky_numbers[i]:
            lucky_numbers[i].append(lucky)
        else:
            while flag:
                lucky = rand_gen((NUM_DIGITS[i]))
                if lucky not in lucky_numbers[i]:
                    flag = False
            lucky_numbers[i].append(lucky)

print("*****************************")
print("Lucky Numbers of 2018")
print("*****************************")

for i in range(len(WINNING_CASES)):
    print(WINNING_CASES_EXPLANATION[i] + ":")
    for j in range(WINNING_CASES[i]):
        print(lucky_numbers[i][j])

while True:
    ticket = input("Please enter the number of your ticket:")
    if (7 == len(ticket)):
        try:
            val = int(ticket)
            break
        except ValueError:
            print("Please enter a valid 7 digit ticket number!")
    else:
        print("Please Enter a valid 7 digit ticket number!")

ticket = str(ticket)

prize = -1
for i in reversed(range(len(WINNING_CASES))):
    for j in range(WINNING_CASES[i]):
        if ticket.endswith(lucky_numbers[i][j]):
            prize = i

if (prize == -1):
    print("Sorry, you won nothing!")
else:
    print("Congratulations, Won - " + WINNING_CASES_EXPLANATION[prize])
