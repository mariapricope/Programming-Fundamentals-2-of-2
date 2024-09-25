# Utils.py

import sys

def get_input(prompt):
    """
    Helper function to get user input and allow exiting by typing 'exit'.
    
    :param prompt: The prompt to display to the user.
    :return: The user's input or exits the program if 'exit' is entered.
    """
    user_input = input(prompt).strip()
    if user_input.lower() == "exit":
        print("Exiting the system.")
        sys.exit()  # Terminate the program
    return user_input
