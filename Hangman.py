import random

HANGMAN = [
    "",
    "  O",
    "  O\n  |",
    "  O\n /|",
    "  O\n /|\\",
    "  O\n /|\\\n  |",
    "  O\n /|\\\n  |\n /",
    "  O\n /|\\\n  |\n / \\",
    " _\n  O\n /|\\\n  |\n / \\",
    "___\n  O\n /|\\\n  |\n / \\"
]

number_of_fails_allowed = 9

with open("words.txt", "r") as f:
    words = f.read().splitlines()

chosen_word = random.choice(words).lower()

hangman_word = []
for i in chosen_word:
    hangman_word.append("_")
print(hangman_word)

word = list(chosen_word)
empty_word = list(hangman_word)
lives = number_of_fails_allowed
guessed = []
wrong_guesses = 0

while lives > 0 and empty_word != word:
    user_letter = str(input("enter a letter or number:\n"))

    if not user_letter.isalnum() or len(user_letter) != 1:
        print("cant put that try again")
        continue

    if user_letter in guessed:
        print("You already tried that.")
        continue

    guessed.append(user_letter)

    if user_letter in word:
        for i in range(len(word)):
            if word[i] == user_letter:
                empty_word[i] = user_letter
        print(empty_word)
    else:
        lives -= 1
        wrong_guesses = number_of_fails_allowed - lives
        print("Wrong. Lives left: " + str(lives))
        print(HANGMAN[wrong_guesses])
        print(empty_word)

if empty_word == word:
    print("You win ! The word was " + chosen_word)
else:
    print(HANGMAN[-1])
    print("you lost ! The word was " + chosen_word)
