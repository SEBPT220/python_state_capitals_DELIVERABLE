from capitals import states
import random
random.shuffle(states)
correct_counter = 0
incorrect_counter = 0
# print(states)

def greet(name):
     player = input("Please enter your name:")
     return f"{name}, {player}! Welcome to the game!"
print(greet("Welcome"))

for state in states:
    if "correct" not in state:
        state["correct"] = 0
    if "incorrect" not in state:
        state["incorrect"] = 0

def incorrect_ans_list(state):
    return state["incorrect"]

def hint(ans):
    return ans[:3]
    

while True:
   
   
   for state in states:
        
        user_answer = input(f"What is the capital of {state["name"]}? or Type 'hint' for a hint:")
        
        
        if user_answer.lower() == state["capital"].lower():
            correct_counter += 1
            # print ("Correct andswer")
            state["correct"] +=1

            print(f"The correct answer! and the total number of corrected answers are now: {correct_counter}")
            print(f"The capital of the {state['name']} is {state['capital']}")
            print(f"The number of correct answers for {state['name']}: {state['correct']}")
        elif user_answer.lower() == "hint":
            hint = hint(state["capital"])
            print(f"The capital starts with '{hint}")
        
        else :
             incorrect_counter += 1
             state["incorrect"] +=1
             print(f"The incorrect answer! and the number of incorrected answeres are now: {incorrect_counter}")
             print(f"The capital of the {state['name']} is {state['capital']}")
             print(f"The number of incorect answers for {state['name']}: {state["incorrect"]}")

   sorted_list = sorted(states, key = incorrect_ans_list, reverse=True)
             
   while True:
        
       ask_user = input(f"Would you like to play again (yes/ no): ")
       play_again = (ask_user == "yes")
       done_play = ( ask_user == "no")

       if play_again : 
         states[:] = sorted_list
         print(f"The highest number of incorrect answers were given on {state['name']}")
         break
       elif done_play  : 
         print("Thankyou for playing")
         exit() 
       else :
           print("Please choose a valid option: 'yes' or 'no'.")
      
      
  




