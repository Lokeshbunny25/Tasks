import random


words = ["python", "computer", "program", "coding", "developer", "test", "handle", "candle"]


word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_incorrect_guesses:

    
        display_word = ""

        for letter in word:
                if letter in guessed_letters:
                        display_word += letter
                else:
                        display_word += "_"

        print("\nWord:", display_word)
        print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

                                                                
        if "_" not in display_word:
                print("Congratulations! You guessed the word:", word)
                break

                                                                                        
        guess = input("Enter a letter: ").lower()

                                                                                                
        if len(guess) != 1 or not guess.isalpha():
                print("Please enter one letter only.")
                continue

        if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

        guessed_letters.append(guess)

                                                                                                                                                
        if guess in word:
                print("Correct guess!")
        else:
                incorrect_guesses += 1
                print("Wrong guess!")

else:
        print("\nGame over!")
        print("The word was:", word)