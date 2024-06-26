'''
HUNTER SITKI
The Elevator

Written for Bluestaq Code Challenge


ASSUMPTIONS:
    - The user is starting on floor 1
    - Max number of floors is 20
    - 1-indexing user and elevator floors for clarity
    - The elevator is being used by others in the building, therefore its floor is random when called
TODOS:
    - More specifically simulating other people using the elevator
    - Have multiple elevators in the building and allow a user to select which one they want to use
    - Add a chance for a random Emergency Event and an elevator button that will call out for help
'''

import random

# ASCII for the visualizations in the program
def elevator_door(floor_number): 
    door = f'''
  ______________
 /      {floor_number}       \\
|________________|
 ________________
|       ||       |
|       ||       |
|       ||       |
|       ||       |
|       ||       |
|       ||       |
|_______||_______|

'''
    print(door)

def elevator_buttons(user, NUM_FLOORS):
    buttons = f'''
______________
      {user}
______________\n
'''
    for i in range (1, NUM_FLOORS+1):   # Base the number of buttons on the total available number of floors
        buttons += f"[{i:02}] " # Use :02 to display a 0 in front of 1-digit numbers for consistent spacing
        if i % 3 == 0:  # Add a new line every 3 buttons
            buttons += "\n"
    print(buttons)


# Function simulating the elevator running and being available at all times.
def run_elevator(user, elev, NUM_FLOORS):
    # Simulate another person using the elevator and leaving it on a random floor
    elev = random.randint(1, NUM_FLOORS)
    elevator_door(elev)
    print(f"Someone has left the elevator on floor {elev}")

    # Keep the elevator ready to be called
    while True:
        user_input = input("Type 'c' to call the elevator, or 'q' if you would like to quit the program\n")
        if user_input.lower() == 'c' or user_input.lower() == 'call':   # Checking the user makes the correct call and accepts valid edge case inputs
            call_elevator(user, elev, NUM_FLOORS)
            break
        elif user_input.lower() == 'q' or user_input.lower() == 'quit': # Option to quit the program
            print("Thank you for using the elevator!")
            exit()
        else:   # Only accept the call or quit as valid input
            print("Invalid input. Please type 'c' to call the elevator, or 'q' if you would like to quit the program\n")

# Function handles displaying the elevator buttons and user selecting their floor
def call_elevator(user, elev, NUM_FLOORS):
    while True:
        elevator_buttons(user, NUM_FLOORS)
        sel_floor = input(f"The elevator has been called from floor {elev} to you on floor {user}. Which floor would you like to go to? (1 - {NUM_FLOORS})\n")
        try:
            sel_floor = int(sel_floor)
            if 1 <= sel_floor <= NUM_FLOORS:
                break
            else:   # Handles a user selecting an int but it being out of the valid range
                print(f"You've selected an invalid floor number. Please select a floor between 1 and {NUM_FLOORS}\n")
        except ValueError:  # Handles a user inputting something other than an int
            print("Invalid input. Please select a floor number")

    print(f"The elevator comes to floor {user}, you get in and it takes you to floor {sel_floor}. Have a nice time here!\n")
    # Setting the elevator and user to the selected floor
    # This is undone for 'elev' by calling run_elevator and having a random floor selected,
    # but maintains the accuracy of the simulation in case a different functionality is wanted later
    elev = sel_floor
    user = sel_floor

    # Put the elevator back into running
    run_elevator(user, elev, NUM_FLOORS)

def main():
    user = 1 # User starts on floor 1, as if they have just entered the building
    MAX_FLOORS = 20
    NUM_FLOORS = random.randint(2, MAX_FLOORS)
    elev = random.randint(1, NUM_FLOORS)
    print(f"\nYou walk up to the elevator in the {NUM_FLOORS} story building and go to the elevator")

    run_elevator(user, elev, NUM_FLOORS)

main()