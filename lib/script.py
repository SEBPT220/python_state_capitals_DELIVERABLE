from capitals import states
import random

def play_game():
    
    random.shuffle(states)
    
    
    correct_answers = 0
    incorrect_answers = 0

    print("Welcome to the State Capitals Game!")

    
    for state in states:
        
        user_answer = input(f"What is the capital of {state['name']}? ").strip()
        
       
        if user_answer.lower() == state['capital'].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect! The capital of {state['name']} is {state['capital']}.")
            incorrect_answers += 1
        
       
        print(f"Correct answers: {correct_answers}, Incorrect answers: {incorrect_answers}")

   
    print(f"Game Over! You got {correct_answers} correct and {incorrect_answers} incorrect.")

    
    play_again = input("Do you want to play again? (yes/no) ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing! Goodbye.")


play_game()
