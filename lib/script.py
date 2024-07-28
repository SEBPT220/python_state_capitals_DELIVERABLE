from capitals import states
import random

def play_again():
    play_again_question = input('Would you like to play again? (yes/no)')
    if play_again_question.lower() == "yes":
        states_game()
    else:
        exit()


def states_game():
    correct = 0
    wrong = 0
    print('Welcome to the states game where you will test your knowledge of the capital of each state!!!')
    initial_question = input('Are you ready to play? (yes/no)')

    if initial_question.lower() == "yes":
        random.shuffle(states)  
        for state in states:
            print(f'Correct: {correct} and Wrong: {wrong}')
            user_input = input(f'What is the capital of {state["name"]}? ')

            if user_input.lower() == state["capital"].lower():
                print('Correct!')
                correct += 1
            else:
                print(f"Incorrect. The capital of {state['name']} is {state['capital']}.")
                wrong += 1

        print(f'Game Over! Final Score: Correct: {correct}, Wrong: {wrong}')
        play_again()

        print("Maybe next time!")
        play_again()


states_game()




