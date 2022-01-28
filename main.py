from random import choice

def main():
    # Diccionary for the game.
    guesses = ["Computer", "Videogame", "Cellphone"]

    # Get a random element for the game.
    chosen_word = choice(guesses)
    print(chosen_word)

    hangman = ['_' for _ in chosen_word]
    users_current_word = "".join(hangman)

    lives = 5

    while users_current_word != chosen_word:
        if lives == 0:
            break

        print("♥" * lives)
        print(users_current_word)
        users_guess = input("Enter a character guess: ")

        if users_guess in chosen_word:
            # Look for al the character coincidences.
            i = 0
            while i < len(chosen_word):
                if chosen_word[i] == users_guess:
                    hangman[i] = users_guess
                i += 1
        else:
            lives -= 1

        users_current_word = "".join(hangman)

    if lives == 0:
        print("Sorry, you lost :(")
    else:
        print(users_current_word, "\nYou won!!!")

main()
