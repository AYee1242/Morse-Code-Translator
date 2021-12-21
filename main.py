# Python program to implement Morse Code Translator

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

MORSE_CODE_DICT_REV = {'.-': 'A', '-...': 'B',
                       '-.-.': 'C', '-..': 'D', '.': 'E',
                       '..-.': 'F', '--.': 'G', '....': 'H',
                       '..': 'I', '.---': 'J', '-.-': 'K',
                       '.-..': 'L', '--': 'M', '-.': 'N',
                       '---': 'O', '.--.': 'P', '--.-': 'Q',
                       '.-.': 'R', '...': 'S', '-': 'T',
                       '..-': 'U', '...-': 'V', '.--': 'W',
                       '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                       '.----': '1', '..---': '2', '...--': '3',
                       '....-': '4', '.....': '5', '-....': '6',
                       '--...': '7', '---..': '8', '----.': '9',
                       '-----': '0', '--..--': ',', '.-.-.-': '.',
                       '..--..': '?', '-..-.': '/', '-....-': '-',
                       '-.--.': '(', '-.--.-': ')'}

# Encrypt the message to morse code


def encrypt(msg):
    msg = msg.upper()
    morse_code = ''
    for letter in msg:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT[letter] + ' '
        # New word
        else:
            morse_code += ' '

    return morse_code

# Decrypt a string


def decrypt(msg):
    msg = msg.upper()

    # msg needs extra space in the end to decrypt the last letter
    msg += ' '

    deciphered_word = ''
    letter = ''
    for morse in msg:

        # checks for space
        if (morse != ' '):
            letter += morse

            # counter to keep track of spaces
            num_spaces = 0

        # in case of space
        else:
            num_spaces += 1

            # new word
            if num_spaces == 2:

                # adding space to separate words
                deciphered_word += ' '
            else:

                # deciphering the letter
                deciphered_word += MORSE_CODE_DICT_REV[letter]
                letter = ''

    return deciphered_word

# Hard-coded driver function to run the program


def main():
    print("Hello! Welcome to my morse code encryption/decryption service")
    while True:
        cmd = input("Please type e for encryption or d for decryption: ")
        if cmd == 'e' or cmd == 'd':
            msg = input("Please enter the message to encrypt/decrypt: ")
            if (cmd == 'e'):
                encrypted_msg = encrypt(msg)
                print(f"The encrypted message is {encrypted_msg}")
            else:
                decrypted_msg = decrypt(msg)
                print(f"The decrypted message is {decrypted_msg}")
            if input("Would you like to encrypt/decrypt another message? Enter y or n: ") != 'y':
                break
        else:
            print("Invalid command! Please try again")


# Executes the main function
if __name__ == '__main__':
    main()
