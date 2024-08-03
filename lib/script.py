from capitals import states
import random

def play_again():
    play_again_prompt = input('Would you like to play again? (yes/no)')
    if play_again_prompt.lower() == 'yes':
        start_game()
    else:
        exit()

def start_game():
    correct_answer = 0
    wrong_answer = 0
    
    print('Welcome! Train your brain with the US Capitals game, type the correct capital city for the state prompted to increase correct counter. Perfect score is 50 correct capitals, good luck!')
    begin_game = input('Ready to start? (yes/no)')

    if begin_game.lower() == 'yes':
        random.shuffle(states)
        for state in states:
            print(f'Correct: {correct_answer} Wrong: {wrong_answer}')
            player_guess = input(f'What is the capital of {state["name"]}? \n You can type "hint" for a hint')

            if player_guess.lower() == 'hint':
                print(f'Here are the first three letters: {state["capital"][:3]}')
                player_guess = input(f'What is the capital of {state["name"]}?')
            
            if player_guess.lower() == state["capital"].lower():
                print(f"That's Correct! The capital of {state['name']} is {state['capital']}.")
                correct_answer += 1
            else:
                print(f"I'm sorry that's incorrect, the capital of {state['name']} is {state['capital']}.")
                wrong_answer += 1
        
        print(f"Game Over! Final Score - Correct: {correct_answer}, Wrong: {wrong_answer}")
        play_again()

start_game()