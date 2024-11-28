def prompt_integer(message):
    final_value = None  # Store the final valid input value from the user
    while final_value is None:  # Loop until a valid input is received
        try:
            final_value = int(input(message))  # Attempt to convert the user input into an integer
        except ValueError:
            # If the input is not a valid integer, prompt the user to enter again
            print("    Invalid input. Please enter a valid integer.")
    return final_value  # Return the valid integer

def prompt_integer_range(message, min_value, max_value):
    final_value = None  # Store the final valid input value from the user
    while final_value is None:  # Loop until a valid input is received
        value = prompt_integer(message)  # Call prompt_integer to get the user's input as an integer
        if min_value <= value <= 5:  # Check if the input is within the specified range
            final_value = value  # If it's in the range, update the valid value
        else:
            # If the input is not in the range, prompt the user to enter again
            print(f"    Invalid input. Please enter a value between {min_value} and {max_value}.")
    return final_value  # Return the valid integer within the range

