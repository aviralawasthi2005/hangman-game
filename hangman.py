import random

def hangman():
    """
    The function "hangman" is likely a Python program that implements the classic word guessing game.
    """
    # List of words for the game
    word_list = ["python", "hangman", "computer", "programming", "algorithm",  "keyboard", "developer", "software", "debugging", "variable"]
    
    # Select a random word
    secret_word = random.choice(word_list).lower()
    guessed_letters = []  # Letters the player has guessed
    word_completion = "_" * len(secret_word)  # Display word with underscores for unguessed letters
    guessed = False
    incorrect_guesses = 0
    max_incorrect = 6  # Maximum allowed incorrect guesses
    
    print("Let's play Hangman!")
    print(display_hangman(incorrect_guesses))
    print(word_completion)
    print("\n")
    
    while not guessed and incorrect_guesses < max_incorrect:
        guess = input("Please guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            guessed_letters.append(guess)
            
            if guess in secret_word:
                print("Good guess!")
                # Update word completion with correctly guessed letters
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                
                if "_" not in word_completion:
                    guessed = True
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                incorrect_guesses += 1
            
            print(display_hangman(incorrect_guesses))
            print(word_completion)
            print(f"Guessed letters: {', '.join(guessed_letters)}")
            print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}\n")
    
    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{secret_word}'. Better luck next time!")

def display_hangman(tries):
    stages = [  # Final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

if __name__ == "__main__":
    hangman()