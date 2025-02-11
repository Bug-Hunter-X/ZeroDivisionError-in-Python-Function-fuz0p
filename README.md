# ZeroDivisionError in Python Function
This repository demonstrates a common error in Python: the `ZeroDivisionError`. The `bug.py` file contains a function that attempts to divide by zero, resulting in this error.  The `bugSolution.py` file shows how to handle this error gracefully using exception handling.

## Problem
The function in `bug.py` doesn't check for a zero denominator, leading to a `ZeroDivisionError` when called with `b=0`. This is a runtime error that crashes the program.

## Solution
The solution in `bugSolution.py` uses a `try-except` block to catch the `ZeroDivisionError`. If the error occurs, it prints an informative message instead of crashing.