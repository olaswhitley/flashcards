from sys import argv
import os
import csv
from pathlib import Path

filename = argv[1]
file_path = Path(filename)

# Create the file and header if necessary
if not file_path.exists() or file_path.stat().st_size == 0:
    side_a = input("A Side: ")
    side_b = input("B Side: ")

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([side_a, side_b])

with open(filename, mode='r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader) 
    prompt_a = headers[0]
    prompt_b = headers[1]

while True:
    os.system("clear")

    a = input(f"{prompt_a}: ")
    b = input(f"{prompt_b}: ")

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([a, b])

    prompt = input("Add another card? y/n: ")

    while prompt != "y" and prompt != "n":
        os.system("clear")
        prompt = input("Please enter y or n: ")

    if prompt == "n":
        break