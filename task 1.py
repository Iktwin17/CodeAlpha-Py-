import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "computer", "program", "random"]
    
    # Randomly choose a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    
    attempts = 6
    guessed_letters = []
    
    print("Welcome to Hangman!")
    print("You have 6 incorrect guesses allowed.")
    
    while attempts > 0 and "_" in guessed_word:
        print("\nWord: " + " ".join(guessed_word))
        print("Guessed letters: ", guessed_letters)
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1
    
    # End of game
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n😢 Out of attempts! The word was:", word)


# Run the game
hangman()
