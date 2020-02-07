# Collatz conjecture - For any positive integer, if it is even, divide by two.
# If it is odd, perform 3x + 1.
# Continue this sequence with each value obtained. Eventally the answer is always 1.

def collatz(orig_number):
    if orig_number == "1":
        # Rebuke the user if they think they're cool and funny.
        print("Enter a number that is NOT 1, smartass.")
    # Change type() of input from string to integer.
    number = int(orig_number)
    if number != 1:
        # Set initial variable to non-positive integer.
        new_number = 0
        if number % 2 == 0:
            # If number is even, divide by two, retaining int type.
            new_number = number // 2
            # Shows output of even input.
            print(new_number)
            # Starts process over with result of even input.
            collatz(new_number)
        elif number % 2 == 1:
            # If number is odd, multiply by 3, then add 1.
            new_number = number * 3 + 1
            # Show output of odd input.
            print(new_number)
            # Starts process over with result of odd output.
            collatz(new_number)
    # Eventual end state.
    elif number == 1:
        print("Collatz complete!")

# Prompt user input and call collatz() using that input.
print("Enter an integer other than 1.")
collatz(input())
