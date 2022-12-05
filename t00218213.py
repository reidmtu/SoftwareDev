def caesar_cipher():
    text = input("Please enter some text: ")  # takes users input as a string
    number = input("Please enter a number between -25 and 25: ")  # -25-1 will be moved left, 0 25 will be moved right
    number = int(number)  # input is converted to int
    result = ""  # when the input is in ciphertext

    for i in range(len(text)):
        char = text[i]  # goes through the inputted string
        if char.isupper():  # for upper letters
            result += chr((ord(char) + number - 65) % 26 + 65)
        else:  # for lower case letters
            result += chr((ord(char) + number - 97) % 26 + 97)
    return result
# caesar_cipher()
