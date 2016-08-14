"""
Ceaser cipher decipher/encipher code.  main prints all transpositions.  Ceaser() takes a text input, dict and returns
ciphertext/plaintext, depending on the specified code dictionary
"""

import string

alpha = string.ascii_lowercase

alltrans_dict = {alpha[x]: dict(zip(alpha[x:] + alpha[:x], alpha)) for x in range(len(alpha))}
def decipher(text, cipherdict):
    """
    takes a text input and transforms that by a simple replacement specified by the given dict
    :param text: probably the ciphertext, but if you put plaintext here, it will encipher it per the dict param
    :param cipherdict: a 1:1 dict lining up a letter with a replacement
    :return: the plaintext/ciphertext after replacement per dict param
    """
    templist = []
    for letter in text:
        if letter.lower() in alpha:
            templist.append(cipherdict[letter.lower()])
        elif letter in string.printable:
            templist.append(letter)
    return "".join(templist)

def main():
    """
    inputs a text file name, transposes all possible ceaser type transpositions and prints out all options.
    :return: nothing
    """

    filename = input("Enter filename, include path if not in same directory: ")
    with open(filename, 'r', encoding = 'utf-8') as f:
        filetext = f.read()
    print(filetext)

    for letter in alpha:
        print(decipher(filetext, alltrans_dict[letter]))


if __name__ == "__main__":
    main()