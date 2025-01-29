import random

word_list = ["shepherd", "tradition", "camel", "repulsive"]

lives = 6
chosen_word = random.choice(word_list)

display = ["_" for _ in chosen_word]
correct_letters = []

# ASCII hangman stages
hangman_stages = [
    """
     -----
     |   |
     |   O
     |  /|\\
     |  / \\
     |
    =========
    """,
    """
     -----
     |   |
     |   O
     |  /|\\
     |  / 
     |
    =========
    """,
    """
     -----
     |   |
     |   O
     |  /|\\
     |  
     |
    =========
    """,
    """
     -----
     |   |
     |   O
     |  /|
     |  
     |
    =========
    """,
    """
     -----
     |   |
     |   O
     |   |
     |  
     |
    =========
    """,
    """
     -----
     |   |
     |   O
     |   
     |  
     |
    =========
    """,
    """
     -----
     |   |
     |   
     |   
     |  
     |
    =========
    """
]

print(" ".join(display))  # Show initial placeholders

game_over = False

while not game_over and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters or guess in display:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
        correct_letters.append(guess)
    else:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")

    print(hangman_stages[lives])  # Show ASCII hangman
    print(" ".join(display))  # Show updated word status

    if "_" not in display:
        game_over = True
        print("🎉 Congratulations! You win! 🎉")
    elif lives == 0:
        print(f"💀 Game over! The word was '{chosen_word}'. Try again!")

