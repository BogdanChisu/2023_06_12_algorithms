"""
Generate a list of 1000 random numbers.
				a. Print prime numbers and their position inside the list
				b. Print odd numbers from even positions inside list
				c. Print even numbers from odd positions inside list
				d. Print sum of prime numbers that have control number between 3 and 7
"""

##############################################################
# STEPS
##############################################################
"""
a. Generate 1000 random numbers in the interval 0 to 10000
    1.1 Initialize an empty list
    1.2 Repeat 1000 times:
        1.1 For each number check if the number is already in the list
        1.2 If the number is in the list, generate another number
"""
from random import randint
from math import sqrt
import sys
sys.path.append('D:\PycharmProjects\02algoritmi_a')
from f02problems import control_digit

def generate_numbers():
    my_list = []
    for i in range(1000):
        list_flag = True
        while list_flag:
            rand_nr = randint(0, 10001)
            if rand_nr not in my_list:
                my_list.append(rand_nr)
                list_flag = False
    return my_list

"""
b. 
    Initialize am empty list for the prime numbers:
    For each number in the random-generated-numbers list:
    b.1 Check if the number is prime:
        b.1.2 initialize a boolean is_prime as True
        b.1.3 initialize a counter variable at 2
        b.1.4 if the current number in the list IS divisible by the counter variable, then 
        b.1.5 the number is not prime
        b.1.6 and you can skip to the next number
        b.1.7 if the current number in the list IS NOT divisible by the counter variable, then
        b.1.8 increment the counter variable and perform the previous step, once again
        b.1.9 if the value of the counter variable is bigger or equal to the square root of the current number in list
        b.1.10 add the number to the prime number list
"""

##########################################################
### print primes###
def is_prime(a_number):
    for i in range(2, int(sqrt(a_number))):
        if a_number % i == 0:
            return False
    return True

def print_primes(number_list):
    prime_list = []
    for nr in number_list:
        if is_prime(nr):
            prime_list.append(nr)
    return prime_list
##########################################################

"""
c. print odd numbers from even positions inside the list

c1. cycle a counter variable through a range that starts at 0, ends at 1000, with a step of 2
    if the number is not divisible by 2, print the number
"""

##########################################################
### print odd numbers on even positions###
def odd_numbers_even_positions(a_number_list):
    odd_nums = []
    for i in range(0, 1000, 2):
        if a_number_list[i] % 2 == 1:
            odd_nums.append(a_number_list[i])
    return odd_nums
##########################################################

"""
c. print even numbers from odd positions inside the list

c1. cycle a counter variable through a range that starts at 1, ends at 1000, with a step of 2
    if the number is divisible by 2, print the number
"""

##########################################################
### print even numbers on odd positions###
def even_numbers_odd_positions(a_number_list):
    even_nums = []
    for i in range(1, 1000, 2):
        if a_number_list[i] % 2 == 0:
            even_nums.append(a_number_list[i])
    return even_nums
##########################################################

"""
d. Print sum of prime numbers that have control number between 3 and 7 => control digit version
    d.1. initialize sum variable with 0
    d.2 for each number in the list check if the number is a prime
    d.3 if the number is a prime, calculate the control digit
    d.4 if the control digit is between 3 and 7 add the current number to the sum
    d.5 print the value of the sum variable
"""

##########################################################
### print sum of prime numbers with control digit between 3 and 7 ###
def control_digit_between_three_and_seven(a_number_list):
    sum = 0
    for nr in a_number_list:
        if is_prime(nr):
            ctrl_digit = control_digit(nr)
            if ctrl_digit >= 3 and ctrl_digit <= 7:
                sum += nr
    return sum
##########################################################

def main():
    print("|-----------------------------------------------|")
    print("|                 Main Function                 |")
    print("|-----------------------------------------------|")

    ##########################################################
    ### print generated numbers ###
    print("\n\n|-----------------------------------------------|")
    print("|                  Numbers generated                  |")
    my_list = generate_numbers()
    print(f"Length of list = {len(my_list)}")
    print(my_list)
    print("|-----------------------------------------------|")
    ##########################################################

    ##########################################################
    ### print generated numbers ###
    print("\n\n|-----------------------------------------------|")
    print("|                  Print primes                  |")
    my_prime_list = print_primes(my_list)
    print(my_prime_list)
    print(f"Prime numbers list length {len(my_prime_list)}")
    print("|-----------------------------------------------|")
    ##########################################################

    ##########################################################
    ### odd_numbers_even_positions ###
    print("\n\n|-----------------------------------------------|")
    print("|                  Print odd numbers on even positions                  |")
    my_odd_list = odd_numbers_even_positions(my_list)
    print(my_odd_list)
    print(f"Length of odd numbers list {len(my_odd_list)}")
    print("|-----------------------------------------------|")
    ##########################################################

    ##########################################################
    ### even_numbers_odd_positions ###
    print("\n\n|-----------------------------------------------|")
    print("|                  Print even numbers on odd positions                  |")
    my_evens_list = even_numbers_odd_positions(my_list)
    print(my_evens_list)
    print(f"Length of even numbers list {len(my_evens_list)}")
    print("|-----------------------------------------------|")
    ##########################################################

    ##########################################################
    ### print sum of prime numbers with control digit between 3 and 7 ###
    print("\n\n|-----------------------------------------------|")
    print("|                  Print sum of prime numbers with control digits between 3 and 7                  |")
    print(f"Sum of prime numbers with control digits between 3 and 7 is \n"
          f"{control_digit_between_three_and_seven(my_list)}.")
    print("|-----------------------------------------------|")
    ##########################################################

if __name__ == '__main__':
    main()