import random

from day7_hangman_words import word_list

from day7_hangman_art import logo, stages
print(logo)

chosen_word = random.choice(word_list)

lives = 6

display = []
n = len(chosen_word)
for _ in range(n):
    display += '_'


end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}\n")
        continue

    for i in range(n):
        letter = chosen_word[i]
        #print(f"Current position: {i}\nCurrent letter: {letter}\n"
              #f"Guessed letter: {guess}")
        if letter == guess:
            display[i] = letter


    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    else:
        print(f"You guessed {guess}, that's not in the word."
              f"You lose a life.")

        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")
            print(f"The correct word is {chosen_word}.")



    print(f"{' '.join(display)}")

    if '_' not in display:
        end_game = True
        print("You win!")

    print(stages[lives])




