###
# Collatz conjecture - For any positive integer, if it is even, divide by two.
# If it is odd, perform 3x + 1.
# Continue this sequence with each value obtained. Eventally the answer is always 1.

def collatz(orig_number):
    if orig_number == "1":
        print("Enter a number that is NOT 1, smartass.")  # Rebuke the user if they think they're cool and funny.
    number = int(orig_number)  # Change type() of input from string to integer.
    if number != 1:
        new_number = 0  # Set initial variable to non-positive integer.
        if number % 2 == 0:
            new_number = number // 2  # If number is even, divide by two, retaining int type.
            print(new_number)  # Shows output of even input.
            collatz(new_number)  # Starts process over with result of even input.
        elif number % 2 == 1:
            new_number = number * 3 + 1  # If number is odd, multiply by 3, then add 1.
            print(new_number)  # Show output of odd input.
            collatz(new_number)  # Starts process over with result of odd output.
    elif number == 1:  # Eventual end state.
        print("Collatz complete!")

# Prompt user input and call collatz() using that input.
print("Enter an integer other than 1.")
collatz(input())
