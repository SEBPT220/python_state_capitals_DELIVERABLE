from capitals import states
import random

def game(states):
    states_list = list(states)
    random.shuffle(states_list)

    correct = 0
    incorrect = 0

    print("Welcome to the Game of State Capitals!")
    print("See if you can guess all of the capitals of each state.")

    for state in states_list:
        guess = input(f"What is the capital of {state['name']}? ")
        if guess.lower() == state['capital'].lower():
            correct += 1
            print("Correct!")
        else:
            incorrect += 1
            print(f"Incorrect! The answer is {state['capital']}.")
        print(f"Current Score: {correct} correct, {incorrect} incorrect.")

    print(f"Final Score: {correct} correct, {incorrect} incorrect.")

    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
        game()
    else:
        print("Bye!")

game(states)