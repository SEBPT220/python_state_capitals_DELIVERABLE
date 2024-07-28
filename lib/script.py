import random
from capitals import states

def play_game():
    # Welcome message
    print("Welcome to the State Capitals Quiz!")

    # Initialize counters
    correct_count = 0
    incorrect_count = 0

    # Shuffle the states to randomize order
    random.shuffle(states)

    # Loop through each state
    for state in states:
        # Prompt user for the capital
        user_answer = input(f"What is the capital of {state['name']}? ").strip()

        # Check if the guess is correct
        if user_answer.lower() == state['capital'].lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect.")
            incorrect_count += 1

        # Display running tally
        print(f"Correct: {correct_count} | Incorrect: {incorrect_count}")

    # Final score
    print("Game Over!")
    print(f"Final Score: Correct: {correct_count} | Incorrect: {incorrect_count}")

    # Ask if the user wants to play again
    play_again = input("Play again? (yes or no) ").strip().lower()
    if play_again == 'yes':
        play_game()

if __name__ == "__main__":
    play_game()
