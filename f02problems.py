"""
######################
### REPRESENTATION ###
	1. Natural Language
		You are given a list of words and a list of numbers.
			1. Print the words that are PALINDROME (palindrome: https://ro.wikipedia.org/wiki/Palindrom):
			2. Print the number and control_digit for each number in the list of numbers (control_digit: https://infoas.ro/lectie/2/cifra-de-control-a-unui-numar)

	2. Code
	3. Pseudocode
		### Palindrome function ###
		is_palindrom = true
        i = 0
        WHILE i < length_word // 2
            if word[i] != word[-1-i]:
                EXIT
            i += 1
        END WHILE
        return is_palindrome
		### Control Number function ###


	4. Block Diagram  ->  https://www.diagrameditor.com/
		### palindrome function ###
		### control number function ###

######################

"""

### palindrome: 1234321, ana, civic, cojoc, minim, radar ###
words_list = ['solo', '1234321', 'ana', 'trotineta', 'civic', 'pisica', 'cojoc', 'maxim', 'minim', 'software', 'radar', 'Camac']

### control digit: ??
numbers_list = [12345, 52314, 12453, 41352, 85432845921, 9, 10, 0, 1]
# 12345 = 1+2+3+4+5 = 15 > 10 =>
                    # 15 => 1 + 5 = 6 < 10



def palindrome(word):

    ##################################################################
    ### steps area ###
    """
    1. for each word in word_list
        1.1 starting from index i equal to 0
        1.2 check if letter at index i is equal to letter at index -1-i
        1.3 increment index i and redo previous step
        1.4 if letters are not identical, word is not palindrome and will not be printed
        1.5 if you reach index i equal to the length of the word integer divided by 2 then print the word
    """
    ##################################################################


    ##################################################################
    ### code area ###
    is_palindrome = True
    word = word.lower()
    for i in range(len(word) // 2):
        if word[i] != word[-1-i]: # de ce nu merge cu word.lower?
            is_palindrome = False
            break

    ### returns TRUE or FALSE ###
    return is_palindrome
    ##################################################################

def sum_digits(another_number):
    str_number = str(another_number)
    sum = 0
    for letter in str_number:
        sum += int(letter)
    return sum

def control_digit(number):

    ##################################################################
    ### steps area ###
    ##################################################################
    """
    for each number in the number list:
    1. convert number to string
    2. initialize sum = 0
    3. each letter in string reconvert to int
    4. add int(letter) to sum
    5. check if sum is > 10
    6. if sum > 10 go to step 1
    7. when new_sum < 10
    8. print new_sum (control_digit)
    """

    ##################################################################
    ### code area ###
    # final_digit = 0
    final_digit = sum_digits(number)
    while final_digit >= 10: # 15
        final_digit = sum_digits(final_digit)

    ### returns the control number ###
    return final_digit
    ##################################################################



def main():

    print("|-----------------------------------------------|")
    print("|                 Main Function                 |")
    print("|-----------------------------------------------|")

    ##########################################################
    ### print Palindromes ###
    print("\n\n|-----------------------------------------------|")
    print("|                  Palindromes                  |")
    for word in words_list:
        if palindrome(word):
            print(word)
    print("|-----------------------------------------------|")
    ##########################################################


    ##########################################################
    ### print number: control_digit ###
    print("\n\n|-----------------------------------------------|")
    print("|                 Control Digit                 |")
    for number in numbers_list:
        print(f"Control digit for number {number} is {control_digit(number)}.")
    print("|-----------------------------------------------|")
    ##########################################################


if __name__ == '__main__':
    main()