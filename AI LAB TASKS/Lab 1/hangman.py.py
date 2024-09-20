import random

def display_hangman(tries):
    stages = [
        "__________      ",
        "|        |      ",
        "|        O      ",
        "|       /|\\     ",
        "|       / \\     ",
        "|               ",
        "|               ",
        "|               ",
    ]
    return "\n".join(stages[:tries+1])

def hangman():
    word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']
    word = random.choice(word_list)
    guessed_letters = set()
    tries = 6
    word_display = '_' * len(word)

    print("Welcome to Hangman!")
    
    while tries > 0 and '_' in word_display:
        print(display_hangman(6 - tries))
        print("Word to guess: " + ' '.join(word_display))
        print("Guessed letters: " + ', '.join(sorted(guessed_letters)))
        print(f"Tries left: {tries}")

        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            word_display = ''.join([letter if letter == guess or letter in guessed_letters else '_' for letter in word])
        else:
            tries -= 1
            print(f"Wrong guess. You lose a try.")
        
        if '_' not in word_display:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print(display_hangman(6 - tries))
        print(f"Sorry, you've run out of tries. The word was: {word}")

hangman()
