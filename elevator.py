import random

'''
ASSUMPTIONS:
    - Max number of floors is 100
    - 1-indexing user and elevator floors for clarity
'''


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
    for i in range (1, NUM_FLOORS+1):
        buttons += f"[{i:02}] "
        if i % 3 == 0:
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

def call_elevator(user, elev, NUM_FLOORS):
    while True:
        elevator_buttons(user, NUM_FLOORS)
        sel_floor = input(f"The elevator has been called from floor {elev} to you on floor {user}. Which floor would you like to go to? (1 - {NUM_FLOORS})\n")
        try:
            sel_floor = int(sel_floor)
            if 1 <= sel_floor <= NUM_FLOORS:
                break
            else:
                print(f"You've selected an invalid floor number. Please select a floor between 1 and {NUM_FLOORS}\n")
        except ValueError:
            print("Invalid input. Please select a floor number")

    print(f"The elevator comes to floor {user}, you get in and it takes you to floor {sel_floor}. Have a nice time here!\n")
    elev = sel_floor
    user = sel_floor

    # Put the elevator back into running
    run_elevator(user, elev, NUM_FLOORS)

def main():
    user = 1
    MAX_FLOORS = 20
    NUM_FLOORS = random.randint(2, MAX_FLOORS)
    elev = random.randint(1, NUM_FLOORS)
    print(f"\nYou walk up to the elevator in the {NUM_FLOORS} story building and go to the elevator")

    run_elevator(user, elev, NUM_FLOORS)

main()