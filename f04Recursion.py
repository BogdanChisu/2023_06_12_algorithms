##############################################
# DEFINITION OF RECURSION
#-------------------------------
"""
Recursion can be understood as an approach to solving a computational problem by calling a function in the body that
implements a solution into itself.

# RECURSION IN REAL LIFE
-------------------------------

An analogy to recursion could be standing in front of a mirror while holding a mirror in your hand. We will then obtain
the effect of going into the mirror.

# RECURSIVE FACTORIAL ALGORITHM
-------------------------------

The function call itself is not a bug, although it may seem so at first. In fact, Python (as well as other programming
languages) will remember there it left off executing the a function to start a new call from the beginning. After the
second order a completes, Python will go back to the first and continue with it.

The simplest example from high-school is the calculation of the factorial:
5! = 5 * 4 * 3 * 2 * 1
n! = n * (n - 1) * (n - 2) * ... * 1
n! = n * (n - 1)!

The definition of factorial can be understood in several ways. The last two examples are fully recursive: the meaning of
the "!" in math is determined by that character. The factorial to be defined calls the factorial (i.e. itself).

A recursive function not only
-----------------
references itself
----------------
but also has
----------------------------------------
a condition that terminates the function
----------------------------------------
and returns the final results.

If it weren't for this postcondition, the recursive function would call itself every time, and we would get an "infinite
loop". This is written in quotation marks because it is not a loop as such and as such and has nothing to do with what
we have seen so far.

The final condition for the factorial is that the input argument is equal to 0 or 1. For these numbers, the factorial is
explicitly defined:

        FINAL CONDITION: 1! = 1
                         0! = 0

--------------------------------------------------
SIMPLE RECURSIVE IMPLEMENTATION
--------------------------------------------------
"""

def factorial(n):
    """
    Calculate factorial
    :param n:
        n: Natural number as input for the algorithm
    :return:
        factorial of number n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

"""
################################
TWO ELEMENTS are important here:
################################

the final condition
-------------------

if n == 0 or n == 1:
    return 1
    
and calling the function itself:
--------------------------------

return n * factorial(n - 1)

############################
HOW DOES IT WORK?
############################

Here's how a recursive algorithm works based on the example of implementing a factorial:
    1. A recursive algorithm is called with an argument, e.g. 5 - factorial(5)
    2. This function checks whether 5 == 0 5 == 1. This is not True as the final result is known - it has to be
       calculated.
    3. The function runs until it calls itself: return n * factorial(n - 1)
    4. Python remembers that it was working on a solution for a function a while before factorial from n = 5, now,
    according to the code, it will call the function factorial(4) (5 - 1 = 4)
    5. The same will happen with factorial(4), factorial(3), factorial(2), factorial(1) - each time the sequence of
    recursive calls will increase. Python will remember the order in which the function was run with each argument
    6. For n = 1 function factorial knows the solution because it is given in the definition. It returns a result, so
    that each previous function can find its own solution and return it to the "higher" function, as shown in the block
    on the right.
    7. Finally, the full result goes to the function launched by the user, i.e. factorial(5)
    
It is EXTREMELY IMPORTANT that Python must use new memory cells with each call - it must store the current result
somewhere and remember where the function was called, how it called the previous function recursively, etc.

Below is an iterative solution to the same problem:
"""

def factorial_iterative(n):
    result = 1
    for i in range(n + 1):
        result *= i
    return result

"""
The ITERATIVE solution is often FASTER because the interpreter does not have to jump between calls of the same function.


INFINITE LOOPS IN RECURSIVE FUNCTIONS:

It is extremely important to remember that recursion is not only about self-induction. It is only necessary to provide a
final condition. Without it Python won't know when to stop calling the same function again. There must be a certain set
of arguments for which the algorithm concludes that it has the solution ready and does not need to recursively compute
it:
"""

def inf_recursion(number):
    if number != 0:
        inf_recursion(number)
    return 0

"""
If we call the function above with the argument 0, nothing bad happens.

If we call the function with an argument different from zero, the situation changes.
The function gets called for an indeterminate number of times.
The function will take up more and more memory to remember previous function calls. Python breaks this vicious cycle and
raises an RecursionError exception when the succesive number of consecutive calls has been reached.


DYNAMIC PROGRAMMING - AN EXAMPLE

The factorial code in a dynamic approach might look like the following 
"""

def factorial_dynamic(n, memory ={0:1, 1:1}):
    """
    Calculates the factorial using a dynamic programming
    :param n: Natural number as input for the algorithm
    :param memory: The dictionary that remembers the results will be updated with each function call
    :return: Factoria of numbers n
    """
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial(n - 1)
        return memory[n]