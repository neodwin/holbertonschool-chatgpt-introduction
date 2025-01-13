#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer `n` recursively.

    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer `n`.
         Returns 1 if `n` is 0 (0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        # Vérification de l'entrée utilisateur
        if len(sys.argv) != 2:
            print("Usage: ./script.py <non-negative integer>")
        else:
            number = int(sys.argv[1])
            if number < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                f = factorial(number)
                print(f"The factorial of {number} is: {f}")
    except ValueError:
        print("Error: Please enter a valid non-negative integer.")
