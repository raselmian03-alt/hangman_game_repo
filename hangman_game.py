
"""Hangman Game - Python"""


import random
# List of possible words
WORDS = ["code", "python", "data", "analysis", "nod", "bootcam"]


# Hangman drawings (0 wrong guesses -> last drawing = game over)
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]


def choose_word():
    """Pick a random word from the list."""
    return random.choice(WORDS)


def show_game_state(secret_word, guessed_letters, wrong_guesses, score):
    """Show hangman picture, word progress, guesses, and score."""
    print("\n" + "=" * 35)
    print(f"Score: {score}")
    print(HANGMAN_PICS[wrong_guesses])

  
    display_word = []
    for char in secret_word:
        if char in guessed_letters:
            display_word.append(char)
        else:
            display_word.append("_")

    print("\nWord:", " ".join(display_word))
    print(f"Wrong guesses: {wrong_guesses}/{len(HANGMAN_PICS) - 1}")

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("=" * 35)


def get_user_letter(guessed_letters):
    """Get a valid single letter from the user."""
    while True:
        letter = input("Enter a letter (a-z): ").strip().lower()

        if len(letter) != 1:
            print("Please enter only ONE letter.")
            

        if not letter.isalpha():
            print("Please enter a letter (not number/symbol).")
        
            

        if letter in guessed_letters:
            print("You already guessed that letter. Try another.")
            

        return letter


def is_word_guessed(secret_word, guessed_letters):
    """Return True if all letters are guessed."""
    return all(ch in guessed_letters for ch in secret_word)


def play_hangman():
    """Play one full game and return the final score."""
    secret_word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    # Score rules
    score = 100  # starting score

    print("\n Welcome to Hangman!")
    print("Scoring:")
    print("+5 points for correct guess")
    print("-10 points for wrong guess")
    print("Win bonus depends on wrong guesses\n")

    while True:
        show_game_state(secret_word, guessed_letters, wrong_guesses, score)

        guess = get_user_letter(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!")
            score += 5
        else:
            print("Wrong!")
            wrong_guesses += 1
            score -= 10

        # Win condition
        if is_word_guessed(secret_word, guessed_letters):
            bonus = max(0, 20 - 2 * wrong_guesses)
            score += bonus
            show_game_state(secret_word, guessed_letters, wrong_guesses, score)
            print(f"\n You WIN! The word was: {secret_word}")
            print(f" Bonus: +{bonus}")
            return score

        # Lose condition
        if wrong_guesses >= max_wrong:
            show_game_state(secret_word, guessed_letters, wrong_guesses, score)
            print(f"\n Game Over! The word was: {secret_word}")
            return score


def main():
    """Play again loop + best score tracking."""
    best_score = None

    while True:
        final_score = play_hangman()

        if best_score is None or final_score > best_score:
            best_score = final_score

        print(f"\n Final Score: {final_score}")
        print(f" Best Score: {best_score}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye!")
            
            break


if __name__ == "__main__":
    main()

