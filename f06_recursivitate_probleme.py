"""
PALINDROM RECURSIV

eliminand treptat prima si ultima litera din cuvant
1234321
23432
343
4 => conditie de oprire LUNGIMEA SIRULUI <= 1
"""

### palindrome: 1234321, ana, civic, cojoc, minim, radar ###
words_list = ['solo', '1234321', 'ana', 'trotineta', 'civic', 'pisica', 'cojoc', 'maxim', 'minim', 'software', 'radar', 'Camac']

### control digit: ??
numbers_list = [12345, 52314, 12453, 41352, 85432845921, 9, 10, 0, 1]

def palindrom_recursiv(string_current):
    is_palindrome = True
    if len(string_current) <= 1:
        return True
    if string_current[0] == string_current[-1]:
        # print(f"Checking {string_current[1: -1: 1]}")
        palindrom_recursiv(string_current[1: -1])
    else:
        is_palindrome = False
    return is_palindrome

"""
### control digit: ??
numbers_list = [12345, 52314, 12453, 41352, 85432845921, 9, 10, 0, 1]

----------------------------
85432845921 => sum of digits
----------------------------
85432845921 % 10 = 1
85432845921 // 10 = 8543284592
----------------------------
8543284592 % 10 = 2
2 + 1 = 3
8543284592 // 10 = 854328459
----------------------------
854328459 % 10 = 9
3 + 9 = 12
854328459 // 10 = 85432845
----------------------------
85432845 % 10 = 5
12 + 5 = 17
85432845 // 10 = 8543284
----------------------------
8543284 % 10 = 4
17 + 4 = 21
8543284 // 10 = 854328
----------------------------
854328 % 10 = 8
21 + 8 = 29
854328 // 10 = 85432
----------------------------
85432 % 10 = 2
29 + 2 = 31
85432 // 10 = 8543
----------------------------
8543 % 10 = 3
31 + 3 = 34
8543 // 10 = 854
----------------------------
854 % 10 = 4
34 + 4 = 38
854 // 10 = 85
----------------------------
85 % 10 = 5
38 + 5 = 43
85 // 10 = 8
----------------------------
8 % 10 = 8
43 + 8 = 51
8 // 10 = 0 => STOP CONDITION

1234
1234 % 10 = 4
1234 // 10 = 123

"""

def recursive_sum_digits(number):
    if number == 0:
        return 0
    number_b = number // 10
    return (number % 10) + recursive_sum_digits(number_b)

def recursive_control_digit(number):
    if number < 10:
        return number
    else:
        new_num = recursive_sum_digits(number)
        return recursive_control_digit(new_num)

def main():
    print("\n\n|----------------------------------------------------|")
    print("|                  Recursive Palindrome               |")
    for a_string in words_list:
        new_string = a_string.lower()
        # print(f"Current word to be checked is: {a_string}")
        if palindrom_recursiv(new_string):
            print(f"Found a palindrome: {a_string}")
    print("|--------------------------------------------------------|")

    print("\n\n|----------------------------------------------------|")
    print("|                  Recursive Control Digit                  |")
    for a_number in numbers_list:
        print(f"Control digit for number {a_number} is {recursive_control_digit(a_number)}")
    print("|--------------------------------------------------------|")

if __name__ == '__main__':
    main()