import csv

filename = "cards/blah.csv" # your CSV or TXT file

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    cards = list(reader)

# asigns the headers(column names) to variables
a_side = reader.fieldnames[0]
b_side = reader.fieldnames[1]

# print(len(cards)) gets number of cards
# print(len(reader.fieldnames)) gets number of columns, which flashcards should be 2
# print(cards[1][a_side]) gets the first side of the card
# print(cards[1][b_side]) gets the second side of the card