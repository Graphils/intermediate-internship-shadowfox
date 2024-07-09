import random
# list of words which are vegetables
words = ["onion", "pepper", "eggplant", "tomato", "lettuce", "cabbage", "kiwi"]

# choose random word of vegetables
word = random.choice(words)

# create a list to store the guessed words
guessed = ["__"]*len(word)

# Create list to store the incorrect guesses
incorrect_guesses = set()

# Number of attempts
attempts = 7

print('WELCOME TOO HANGMAN YOUR FAVORITE GUESSING GAME')
print("TODAY'S GUESSING WORDS ARE VEGETABLES")
print("YOU HAVE A TOTAL OF 7 ATTEMPTS TO GUESS THE WORD CORRECTLY")

while attempts > 0 and "__" in guessed:
    print("".join(guessed))
    print("Incorrect guesses:", ",".join(incorrect_guesses))
    guess = input("GUESS LETTER:").lower()

    if len(guess) != 1:
        print("Please guess a single letter.")
    elif guess in guessed or guess in incorrect_guesses:
        print("you already have guesses this letter".upper())
    elif guess not in words:
        attempts -= 1
        incorrect_guesses.add(guess)
        print("That letter is not in the word")
    else:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess

if "__" not in guessed:
    print("congratulations , the word", word)
else:
    print("sorry you ran out of attempt!!. The word was".upper(), word)
