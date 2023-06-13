import sys
import time
sys.setrecursionlimit(10**6)

def factorial_recursiv(number):

    if number == 1:
        return 1

    # print(f"Execute factorial recursive({number})")
    return number * factorial_recursiv(number - 1)

"""
---------------------------------------
index:  1 2 3 4 5 6 7 8  9  10
number: 0 1 1 2 3 5 8 13 21 34
---------------------------------------
"""

def fibonacci_iterativ(number):
    if number == 1:
        return 0
    if number == 2:
        return 1
    x = 0
    y = 1
    for i in range(2, number):
        z = x + y
        x = y
        y = z
    return z

def fibonacci_recursiv(number):

    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci_recursiv(number - 1) + fibonacci_recursiv(number - 2)

def main():
    start = time.time()
    print(factorial_recursiv(1000))
    end = time.time()
    print(f"Time = {end - start}")

    print(f"Fibonacci iterativ {fibonacci_iterativ(9)}")
    print(f"Fibonacci recursiv {fibonacci_recursiv(9)}")


if __name__ == '__main__':
    main()