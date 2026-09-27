# Flashcards

A simple command-line flashcard program written in Python.

I built this project as a way to practice Python while creating something I could actually use to study French.

## Features

- Create flashcard CSV files
- Add flashcards to existing files
- Quiz yourself using your flashcards

## Requirements

- Python 3

## Usage

### Creating a flashcard file

Run:

`python3 add.py <flashcard-file>`

The program will ask you for the two sides of the flashcard
and then allow you to add cards.

### Quizzing using a flashcard file

Run:
`python3 quiz.py <flashcard-file> [number-of-questions]`

`<flashcard-file>` is the CSV file containing your flashcards.
`[number-of-questions]` is optional. If you don't provide it, the quiz defaults to 10 questions.