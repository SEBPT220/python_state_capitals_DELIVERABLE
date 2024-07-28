from capitals import states
from random import randrange

def game(states):
    print('Welcome to the state capitals game! Please enter your name:')
    name = input()
    print(f"Hello {name}, let's get started!")

    tracker = {state['name']: 0 for state in states}

    def round(state):
        print(f"What is the capital of {state['name']}?")
        ans = input()
        if ans == state['capital']:
            tracker[state['name']] = 0
            print('You are correct!')
            return True
        else:
            tracker[state['name']] += 1
            print('Incorrect! Hint? (Y/N)')
            hint = input()
            if hint.lower() == 'y':
                print(f'The first 3 letters of the capital of {state["name"]} are {state["capital"][:3]}')
                return round(state)
            else:
                print('Skip? (Y/N)')
                skip = input()
                if skip.lower() == 'y':
                    return False
                else:
                    return round(state)

    cont = 'y'
    last_skipped_state = None
    while cont.lower() == 'y':
        if any(value != 0 for value in tracker.values()):
            sorted_states = sorted(tracker, key=tracker.get, reverse=True)
            for state_name in sorted_states:
                if state_name != last_skipped_state:
                    state = next(state for state in states if state['name'] == state_name)
                    break
        else:
            state = states[randrange(50)]
        
        was_correct = round(state)
        if not was_correct:
            last_skipped_state = state['name']
        else:
            last_skipped_state = None

        print('Continue? (Y/N)')
        cont = input()
        if cont.lower() == 'n':
            break

#print(states)
game(states)