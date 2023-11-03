import random

# Define the options:
options = ['rock', 'paper', 'scissors']

# Initialize the player's score:
score = 0

while True:
    # Get the user's choice:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Validate the user's choice:
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # Generate a random choice for the computer:
    computer_choice = random.choice(options)

    print(f"\nUser choice: {user_choice}")
    print(f"Computer choice: {computer_choice}\n")

    # Determine the winner:
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        score += 1
    else:
        print("You lose!")

    # Ask the user if they want to play again:
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

# Print the player's score:
print(f"\nYour score: {score}")
