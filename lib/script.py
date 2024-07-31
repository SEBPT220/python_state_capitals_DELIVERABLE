from capitals import states
import random

# Initialize correct and incorrect keys for each state
for state in states:
    state['correct'] = 0
    state['incorrect'] = 0

class StateQuiz:
    def __init__(self, state_name, capitals, answer):
        self.state_name = state_name
        self.capitals = capitals
        self.answer = answer

class Game:
    def __init__(self):
        self.rightTallies = 0
        self.wrongTallies = 0
        self.gameStates = states

    def randomState(self):
        # Sort states by incorrect attempts first
        self.gameStates.sort(key=lambda x: x['incorrect'], reverse=True)
        
        # Select one random state for the state name
        random_state = random.choice(self.gameStates)
        state_name = random_state['name']
        state_capital = random_state['capital']
        answer = state_capital

        # Ensure the capital of the selected state is included in the list of four capitals
        remaining_states = [state for state in self.gameStates if state['name'] != state_name]
        random_states_for_capitals = random.sample(remaining_states, 3)  # Get 3 other random states
        capitals = [state['capital'] for state in random_states_for_capitals]
        capitals.append(state_capital)  # Include the capital of the selected state

        # Shuffle the capitals list to ensure the selected state's capital is randomly positioned
        random.shuffle(capitals)

        return StateQuiz(state_name, capitals, answer)

    def checkChoice(self, userInput, capitals, answer, state):
        if userInput == answer:
            self.rightTallies += 1
            state['correct'] += 1  # Increment the correct key
            print('Correct!')
            # Remove the state from gameStates
            self.gameStates = [s for s in self.gameStates if s['name'] != state['name']]
            return True
        else:
            self.wrongTallies += 1
            state['incorrect'] += 1  # Increment the incorrect key
            print(f"Incorrect. The correct capital is {answer}.")
            return False

    def gameStart(self):
        print("Welcome to State Matcher")
        print("Your goal is to match the correct capital to the state.")
        
        while self.gameStates:
            quiz = self.randomState()
            print("\nState:", quiz.state_name)
            print("Capitals:", quiz.capitals)
            
            userInput = input("Choose the capital (or type 'hint' for a hint): ")
            if userInput.lower() == 'hint':
                print(f"Hint: The first 3 letters of the capital are {quiz.answer[:3]}")
                userInput = input("Choose the capital: ")
            
            state = next(s for s in self.gameStates if s['name'] == quiz.state_name)
            if self.checkChoice(userInput, quiz.capitals, quiz.answer, state):
                continue
            else:
                print("Try again.")
        
        print("\nCongratulations! You've matched all the states!")
        print(f"Right Tallies: {self.rightTallies}")
        print(f"Wrong Tallies: {self.wrongTallies}")

# Example usage
game = Game()
game.gameStart()
