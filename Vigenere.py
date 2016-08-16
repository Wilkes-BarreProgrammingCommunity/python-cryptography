"""
takes a textfile as input and prints out either ciphertext or plaintext depending on selected dictionary module
"""

import string

alpha = string.ascii_lowercase

decipher_dict = {alpha[x]: dict(zip(alpha[x:] + alpha[:x], alpha)) for x in range(len(alpha))}
encipher_dect = {alpha[x]: dict(zip(alpha, alpha[x:] + alpha[:x])) for x in range(len(alpha))}



def cipher_letter(letter, cipher_dict, code_counter, codephrase):
    return cipher_dict[codephrase[code_counter]][letter]

def main():
    """
    inputs a text file name, transposes all possible ceaser type transpositions and prints out all options.
    :return: nothing
    """

    filename = input("Enter filename, include path if not in same directory: ")
    with open(filename, 'r', encoding='utf-8') as f:
        filetext = f.read().lower()

    codephrase = input("Enter the code phrase (no spaces or punctuation): ").lower()

    encoding = ""
    while encoding not in ["e", "d"]:
        encoding = input("Decipher or Encipher? (enter D or E): ").lower()
    if encoding == 'e':
        c_dict = encipher_dect
    else:
        c_dict = decipher_dict

    temptext = []
    code_counter = -1

    for letter in filetext:
        if letter in alpha:
            code_counter += 1
            if code_counter == len(codephrase):
                code_counter = 0
            temptext.append(cipher_letter(letter, c_dict, code_counter, codephrase))
        elif letter in string.printable:
            temptext.append(letter)

    print("".join(temptext))


if __name__ == "__main__":
    main()

