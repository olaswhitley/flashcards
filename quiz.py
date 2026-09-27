import csv
import os
from sys import argv
import random

filename = argv[1] # your CSV or TXT file

question_range = 10

os.system('clear')

try:
    question_range = int(argv[2])
    print("Question range is", question_range)
except:
    print("Question range is", question_range)

input()

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    cards = list(reader)

# asigns the headers(column names) to variables
a_side = reader.fieldnames[0]
b_side = reader.fieldnames[1]

for x in range(question_range):
    os.system("clear")
    number_for_question = random.randrange(len(cards))
    if random.randrange(2) == 0:
        print(f"{a_side}: {cards[number_for_question][a_side]}")
        input(f"{b_side}: ")
        print(f"Answer: {cards[number_for_question][b_side]}")
        input()

    else:
        print(f"{b_side}: {cards[number_for_question][b_side]}")
        input(f"{a_side}: ")
        print(f"Answer: {cards[number_for_question][a_side]}")
        input()

os.system("clear")