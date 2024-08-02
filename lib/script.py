from capitals import states
# import random 
import random

restart = True
while restart:
    random.shuffle(states)
    wrong = 0
    correct = 0
    print("""===============WELCOME=====================""")

    question = input("Would you like to play the capital quiz game? [Yes/No]")
    if question == "No":
        restart = False
        print("Oh...Okay")

    if question == "Yes":
        print("You'll be asked to guess the capital of the 50 states. Let's start!")
        for state in (states[:50]):
            question = input("What is the capital of " + state["name"]+ "? ")
            if question != state["capital"]:
                wrong = wrong + 1 
                print("Wrong answer. Try again!")
            if question == state["capital"]:
                correct = correct + 1
                print("Correct answer. You've earned one point!")
        print("Game over ", "You have", correct, "answers and",  (wrong), "answers" )
        question = input("Do you want to play again? [Yes/No]")
        if question == "Yes":
            restart = True
        if question == "No":
            print("Bye. See you next time!")
            restart = False


print(len(states))