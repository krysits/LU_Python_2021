import random

words = ["hangman", "programming", "linux", "strawberry", "latvia"]


def hanging(step):
    if step == 0:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
    elif step == 1:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
    elif step == 2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
    elif step == 3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
    elif step == 4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print("      |")
        print("      |")
    elif step == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" /    |")
        print("      |")
    elif step == 6:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("      |")
    else:
        pass
    print('=' * 10, "\n")


def add_word():
    global words
    words.append(input("New word add to list: "))


def print_word(word, letters):
    positions = '-' * len(word)
    result = ''
    for i, data in enumerate(positions):
        if word[i] in letters:
            result += word[i]
        else:
            result += '-'
    print(result)


def check_word(word, letters):
    positions = '-' * len(word)
    result = ''
    for i, data in enumerate(positions):
        if word[i] in letters:
            result += word[i]
        else:
            result += '-'
    return '-' not in result


def play():
    steps = 0
    user_wins = False
    random_word = random.choice(words)
    guessed_letters = {}
    while steps <= 6:
        hanging(step=steps)
        if steps == 6:
            break
        print("Guessed letters: ", ', '.join(guessed_letters), "\n")
        print_word(word=random_word, letters=guessed_letters)
        letter = input("Enter letter: ")
        if len(letter) > 1:  # just take first letter
            letter = letter[0]

        if letter in guessed_letters:  # already guessed
            print("You lose one guess!")
        guessed_letters[letter] = letter
        if letter in random_word:
            if check_word(random_word, guessed_letters):
                user_wins = True
                break
        else:
            steps += 1

    # end session
    print('=' * 10, "\n")
    print(random_word, "\n")
    if user_wins:
        print("You win!", "\n")
    else:
        print("You lose!", "\n")


game_on = True
while game_on:
    choice = input("Enter 1 to play hangman, 2 to add a new word, 3 to quit program\nEnter number: ")

    if choice[0] in ['1', '2', '3']:
        choice = int(choice[0])
    else:
        choice = 0

    if choice == 1:
        play()
    elif choice == 2:
        add_word()
    elif choice == 3:
        game_on = False
    else:
        print("Not valid choice. Exiting.")
        game_on = False
