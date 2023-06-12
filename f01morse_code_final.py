"""
######################
### ALGORITHM ###
	Algorithm = a formula for solving a computational problem.
	Algorithm = a series of operations carried out using various data structures to solve a programming problem.
######################


######################
### PROCEDURE ###
	1. Problem / task formulation
	2. Determining the input data
	3. Determining the result
	4. Finding a method to complete the task
	5. Expressing the algorithm by using the selected method
	6. Analysing and testing the algorithm
	7. Evaluating the effectiveness of the algorithm
######################


######################
### REPRESENTATION ###
	1. Natural Language
		You are given a dictionary with MORSE DECODE (MORSE_TO_CHR -> code: letter) and a list of codes.
		Create a function for each task:
			a. create a dictionary with with MORSE CODE (CHR_TO_MORSE -> letter:code)
			b. decode a list with morse codes and save it to another list
			c. code again the list generated at b. and see if it is the same as original
	2. Code
	3. Pseudocode
		### FOR block from decode_morse function ###
		final_sentence =  ""

		FOR EACH word IN my_words_list
			my_letters_list = word.split("   ")

			FOR EACH letter IN my_letters_list
					IF letter == "" THEN
						SKIP
					ELSE
						IF letter NOT IN MORSE_TO_CHR then
							print error

						ELSE
							concatenate letter to final_sentence
			END FOR
		END FOR
	4. Block Diagram  ->  https://www.diagrameditor.com/
		### code_morse function code block ###
######################

"""
MORSE_TO_CHR = {
	'.-': 'A', #-> 'A': '.-'
	'-...': 'B', 
	'-.-.': 'C', 
	'-..': 'D',
	'.': 'E', 
	'..-.': 'F', 
	'--.': 'G', 
	'....': 'H', 
	'..': 'I',
	'.---': 'J', 
	'-.-': 'K', 
	'.-..': 'L', 
	'--': 'M', 
	'-.': 'N',
	'---': 'O', 
	'.--.': 'P', 
	'--.-': 'Q', 
	'.-.': 'R', 
	'...': 'S', 
	'-': 'T', 
	'..-': 'U', 
	'...-': 'V', 
	'.--': 'W', 
	'-..-': 'X', 
	'-.--': 'Y', 
	'--..': 'Z', 
	'-----': '0', 
	'.----': '1',
	'..---': '2', 
	'...--': '3', 
	'....-': '4', 
	'.....': '5', 
	'-....': '6',
	'--...': '7', 
	'---..': '8', 
	'----.': '9', 
	'.-.-.-': '.', 
	'--..--': ',', 
	'..--..': '?',
	'.----.': "'", 
	'-.-.--': '!', 
	'-..-.': '/', 
	'-.--.': '(', 
	'-.--.-': ')', 
	'.-...': '&',
	'---...': ':', 
	'-.-.-.': ';', 
	'-...-': '=', 
	'.-.-.': '+', 
	'-....-': '-', 
	'..--.-': '_',
	'.-..-.': '"', 
	'...-..-': '$', 
	'.--.-.': '@', 
	'...---...': 'SOS'
}

CHR_TO_MORSE = dict()
	

def decode_morse(morse_text):

	##################################################################
	### split string by 3 spaces ###
	### for each letter in each word ###
	### search letter in MORSE_TO_CHR dictionary ###
	### if letter not in dictionary then ERR ###
	### if letter in dictionary then append letter to final sentence ###
	##################################################################


	##################################################################
	### code area ###

	global MORSE_TO_CHR

	my_words_list = morse_text.split("   ")
	final_sentence = ""

	for word in my_words_list:
		my_letters_list = word.split(" ")

		for letter in my_letters_list:
			if letter == "":
				continue

			if letter not in MORSE_TO_CHR:
				print(f"LETTER: {letter} was not found in dictionary!")
				return

			else:
				final_sentence += MORSE_TO_CHR[letter]
		
		final_sentence += " "

	final_sentence = final_sentence[:-1]


	print(f"\n{morse_text} = {final_sentence}\n")
	return final_sentence
	##################################################################


def get_reversed_morse_code_chr():

	########################################
	### for each element in MORSE_TO_CHR ###
	### get CHR_TO_MORSE corespondent ###
	########################################


	########################################
	### code area ###
	global MORSE_TO_CHR
	global CHR_TO_MORSE

	for code in MORSE_TO_CHR:
		letter = MORSE_TO_CHR[code]
		CHR_TO_MORSE[letter] = code
	########################################


def code_morse(normal_text):

	##################################################################
	### split string by 1 spaces ###
	### for each letter in each word ###
	### search letter in CHR_TO_MORSE dictionary ###
	### if letter not in dictionary then ERR ###
	### if letter in dictionary then append letter to final sentence ###
	##################################################################


	##################################################################
	### code area ###

	global CHR_TO_MORSE

	my_words_list = normal_text.split(" ")
	final_sentence = ""

	for word in my_words_list:

		for letter in word:

			if letter not in CHR_TO_MORSE:
				print(f"LETTER: {letter} was not found in dictionary!")
				return

			else:
				final_sentence += f"{CHR_TO_MORSE[letter]} "
		
		final_sentence += "   "


	print(f"\n{normal_text} = {final_sentence}\n")

	##################################################################


def main():

    print("|-----------------------------------------------|")
    print("|                 Main Function                 |")
    print("|-----------------------------------------------|")

    list_to_decode = ['.... . -.--   ... --- .-.. ---', ' . ', '...   ---   ...']
    list_to_code = []


    ##########################################################
    ### function that get reversed dictionary ###
    get_reversed_morse_code_chr()
    ##########################################################


    ##########################################################
    ### decode MORSE ###
    print("\n\n|-----------------------------------------------|")
    print("|                 Decode Morse                  |")
    for coded_sentence in list_to_decode:
    	decoded_sentence = decode_morse(coded_sentence)
    	list_to_code.append(decoded_sentence)
    print("|-----------------------------------------------|")
    ##########################################################


    ##########################################################
    ### coding MORSE ###
    print("\n\n|-----------------------------------------------|")
    print("|                 Coding Morse                  |")
    for sentence_to_code in list_to_code:
    	code_morse(sentence_to_code)
    print("|-----------------------------------------------|")
    ##########################################################


if __name__ == '__main__':
    main()