# Blackjack - CS50P Final Project

This project is a simple command-line Blackjack game written in Python as my final project for CS50P. The goal was to create a clean, functional program that implements the core rules of Blackjack: dealing cards, calculating hand values, handling Aces as 1 or 11, and determining the winner at the end of a round. The game intentionally focuses on the essentials to keep the logic clear, structured, and easy to test.

The player always starts with two cards. Afterwards, the player can choose to **hit** to draw another card or **stand** to keep their current total. The dealer then draws cards automatically until reaching at least 17 points. Once both sides are done, the program compares the final hands and prints the result. Aces are counted dynamically as 11 or 1, depending on which value produces the best valid hand.

---

## Files

### project.py
This is the main file that contains the complete game logic, split into small, testable functions:

- `main()`
  Runs a full round of Blackjack, prints the game flow, and handles all user input.

- `create_deck()`
  Builds a standard 52-card deck. Cards are stored as strings like `"A♠"` or `"10♥"`, which keeps the deck simple and easy to display.

- `hand_value(hand)`
  Calculates the value of any given hand. This function correctly handles all Ace scenarios and decides whether an Ace should count as 11 or 1.

- `is_bust(hand)`
  Returns `True` if the hand value is over 21.

The separation between game flow and logic makes the code easier to read and test.

---

### test_project.py
This file contains unit tests written with `pytest`.
The tests cover:

- multiple cases for `hand_value()`
  (normal hands, hands with one Ace counted as 11, one Ace counted as 1, two Aces, mixed-value hands)
- `is_bust()` with both busting and non-busting hands

These tests verify that the core Blackjack logic works as expected, independent of user interaction.

---

## Design Choices

The project is intentionally minimal: no chips, no betting system, and no advanced features such as Split or Double Down. The focus is on writing clean functions, handling tricky cases like Aces, and making the core of the game reliable.

Cards are represented as simple strings rather than objects or classes. This keeps the code lightweight, easy to understand, and perfect for a terminal-based program.
The Ace-handling logic is the most complex part of Blackjack, so I isolated it into its own function to make it easier to test.

All functions are designed to be modular and reusable, which also makes the program easier to extend in the future.

---

## How to Run

```bash
python3 project.py
