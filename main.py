import random

word_list = [
    "umbrella", "pyramid", "laptop", "satellite", "avocado", "volcano", "whistle", "oxygen",
    "giraffe", "elephant", "tiger", "panther", "rhinoceros", "dolphin", "octopus",
    "banana", "pineapple", "watermelon", "strawberry", "blueberry", "mango",
    "canada", "brazil", "sweden", "egypt", "japan", "australia", "germany",
    "keyboard", "backpack", "airplane", "spaceship", "mountain", "notebook",
    "microscope", "hurricane", "galaxy", "bicycle", "headphones", "telescope",
    "treasure", "wizard", "puzzle", "parachute", "robot", "fireworks", "maze",
    "cactus", "glacier", "comet", "gravity", "desert", "rainbow", "castle"
]
secret_word = random.choice(word_list)
max_attempts = 3
attempts = 0
guessed_correctly = False

print("🔍 Welcome to the Word Guessing Game!")
print(f"You have {max_attempts} tries to guess the secret word.\n")

while attempts < max_attempts and not guessed_correctly:
    guess = input("Enter your guess: ").strip().lower()
    attempts += 1

    if guess == secret_word.lower():
        guessed_correctly = True
        break
    else:
        print(f"❌ Incorrect! Attempts left: {max_attempts - attempts}")

if guessed_correctly:
    print("\n🎉 You guessed it! You win!")
else:
    print(f"\n💀 Out of guesses! The word was '{secret_word}'.")
print("Thanks for playing! 🎮")