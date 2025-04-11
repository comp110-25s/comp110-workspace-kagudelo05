"""Exercse 02 Wordle: Katherine Agudelo-Marin"""

__author__: str = "730655640"


def contains_char(search_string: str, character: str) -> bool:
    "Checks if given character is present in string"
    assert len(character) == 1, f"len('{character}') is not 1"
    for char in search_string:
        if char == character:
            return True
    return False


# Define constants for emoji representations of guess accuracy
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns an emoji string repsenting accuracy of Wordle guess."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result = ""
    for idx in range(len(guess)):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX  # Correct letter in the correct position
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX  # Correct letter in the wrong position
        else:
            result += WHITE_BOX  # Incorrect letter
    return result


def input_guess(expected_length: int) -> str:
    """Prompts the useer for a guess of the expected length."""
    guess = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return f"{guess}"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns = 6  # Max number of turns possible
    current_turn = 1  # Initialize turn counter
    while current_turn <= max_turns:
        print(f"=== Turn {current_turn}/{max_turns}===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {current_turn}/{max_turns} turns!")
            return
        current_turn += 1  # Move to next turn
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
