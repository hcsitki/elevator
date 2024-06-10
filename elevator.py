import random

'''
ASSUMPTIONS:
    - Max number of floors is 100
    - 1-indexing user and elevator floors for clarity
'''


'''
Function simulating the elevator running and being available at all times.
'''
def run_elevator(user, elev):
    print(f"\nYou walk up to the elevator in the {NUM_FLOORS} story building. Currently, the elevator is on floor {elev}")

    # Keep the elevator ready to be called
    while True:
        user_input = input("Type 'c' to call the elevator, or 'q' if you would like to quit the program\n")
        if user_input.lower() == 'c' or user_input.lower() == 'call':   # Checking the user makes the correct call and accepts valid edge case inputs
            call_elevator(user, elev)
            break
        elif user_input.lower() == 'q' or user_input.lower() == 'quit': # Option to quit the program
            exit()
        else:   # Only accept the call or quit as valid input
            print("\nInvalid input. Please type 'c' to call the elevator, or 'q' if you would like to quit the program\n")
    
    # Simulate another person using the elevator and leaving it on a random floor
    elev = random.randint(1, NUM_FLOORS)

def call_elevator(user, elev):

    while True:
        sel_floor = input(f"The elevator has been called from floor {elev} to you on floor {user}. Which floor would you like to go to? (1 - {NUM_FLOORS})\n")
        try:
            sel_floor = int(sel_floor)
            if 1 <= sel_floor <= NUM_FLOORS:
                break
            else:
                print(f"You've selected an invalid floor number. Please select a floor between 1 and {NUM_FLOORS}\n")
        except ValueError:
            print("Invalid input. Please select a floor number")

    print(f"The elevator comes to floor {user}, you get in and it takes you to floor {sel_floor}")

    elev = sel_floor
    user = sel_floor

    # Put the elevator back into running
    run_elevator(user, elev)


user = 1
MAX_FLOORS = 100
NUM_FLOORS = random.randint(2, MAX_FLOORS)
elev = random.randint(1, NUM_FLOORS)

run_elevator(user, elev)