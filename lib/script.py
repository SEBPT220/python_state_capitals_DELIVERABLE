from capitals import states
import random

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

    def checkChoice(self, userInput, capitals, answer, state_name):
        if userInput == answer:
            self.rightTallies += 1
            # Remove the state from gameStates
            self.gameStates = [state for state in self.gameStates if state['name'] != state_name]
            print('Correct!,', len(self.gameStates), "States left to match")
            return True
        else:
            self.wrongTallies += 1
            print(f"Incorrect. The correct capital is {answer}.")
            return False

    def gameStart(self):
        print("Welcome to State Matcher")
        print("Your goal is to match the correct capital to the state.")
        while self.gameStates:
            quiz = self.randomState()
            print("\nState:", quiz.state_name)
            print("Capitals:", quiz.capitals)
            userInput = input("Choose the capital: ")
            if self.checkChoice(userInput, quiz.capitals, quiz.answer, quiz.state_name):
                continue
            else:
                # Give another chance if incorrect
                print("Try again.")
        
        print("\nCongratulations! You've matched all the states!")
        print(f"Right Tallies: {self.rightTallies}")
        print(f"Wrong Tallies: {self.wrongTallies}")

# Example usage
game = Game()
game.gameStart()
