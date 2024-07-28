from capitals import states
import random

class Game():
    def __init__(self,):
        self.rightTallies = 0
        self.wrongTallies = 0
        self.gameStates = states

    def randomState(self):
        # Select one random state for the state name
        random_state = random.choice(self.gameStates)
        state_name = random_state['name']
        state_capital = random_state['capital']
        answer = random_state['capital']

        # Ensure the capital of the selected state is included in the list of four capitals
        remaining_states = [state for state in self.gameStates if state['name'] != state_name]
        random_states_for_capitals = random.sample(remaining_states, 3)  # Get 3 other random states
        capitals = [state['capital'] for state in random_states_for_capitals]
        capitals.append(state_capital)  # Include the capital of the selected state

        # Shuffle the capitals list to ensure the selected state's capital is randomly positioned
        random.shuffle(capitals)

        return state_name, capitals, answer
    
    # def checkChoice(self, userInput, currentStates):
    #     if userInput in currentStates:
    #         self.rightTallies += 1
    #         print(f"Correct Capital{}")
    
    
    def gameStart(self):
        print("Welcome to State Matcher")
        print("Your goal is to match the correct capital to the State")
        currentStates= self.randomState()
        print(currentStates.capitals)
        userInput = input("Chosse a state: ")






game = Game()

game.gameStart()
        