import random
from capitals import states

states_correct_incorrect = {state['name']: {'correct': 0, 'incorrect': 0} for state in states}

def play_game():
    welcome_message()
    while True:
        start_quiz()
        if not play_again():
            break

def welcome_message():
    print("Welcome! Here you'll be tested on your State Capital knowledge.")
    print("Let's see how well you know the capitals of all 50 states!\n")
    print("Good luck!!!\n")

def start_quiz():
    correct_answers = 0
    incorrect_answers = 0
    random.shuffle(states)

    for state in states:
        state_name = state['name']
        capital = state['capital']
        answer = input(f"What is the capital of {state_name}? ").strip()
        if answer.lower() == capital.lower():
            print("Correct!\n")
            correct_answers += 1
            states_correct_incorrect[state_name]['correct'] += 1
        else:
            print(f"Incorrect! The capital of {state_name} is {capital}.\n")
            incorrect_answers += 1
            states_correct_incorrect[state_name]['incorrect'] += 1
        
        print(f"Correct: {correct_answers}")
        print(f"Incorrect: {incorrect_answers}\n")

    print("\nQuiz complete!")
    print(f"Your final score is {correct_answers} correct answers and {incorrect_answers} incorrect answers.")

def play_again():
    while True:
        choice = input("Would you like to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        print("Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
