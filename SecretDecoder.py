#f(x) = 5x - 1
letter_dict = {}
encoded_array = {}

#Create index of letters
for i in range(26):
    letter_dict[chr(ord('A') + i)] = i + 1
letter_dict[' '] = 27

def Encode(message):
    encoded_array = []
    for i in message:
        #Convert letter to Number
        number = LetterToNumberLookup(i)

        #encode the number
        encoded_number = 5*number - 1

        #add to encrypted message
        encoded_array.append(encoded_number)
    return encoded_array

def PartialEncode(message):
    converted_array = []
    for i in message:
        #Convert letter to Number
        number = LetterToNumberLookup(i)
        #add to encrypted message
        converted_array.append(number)
    return converted_array

def Decode():
    print("Enter each number of the encoded message, seperated by a space: i.e 45 10 1")
    encoded_message = input()
    encoded_array = encoded_message.split()
    decoded_message = ""
    for i in encoded_array:
        number = int(i)
        decoded_number = (number + 1)/5
        decoded_message += NumberToLetterLookup(decoded_number)
    return decoded_message

def PartialDecode():
    encoded_message = input()
    encoded_array = encoded_message.split()
    converted_message = ""
    for i in encoded_array:
        number = int(i)
        converted_message += NumberToLetterLookup(number)
    return converted_message

def NumberToLetterLookup(number):
    for key, value in letter_dict.items():
        if value == number:
            return key
        
def LetterToNumberLookup(letter):
    return letter_dict[letter.upper()]
    


while True:
    print("         ** MM212 SECRET DECODER TOOL **")
    print("         TOP SECRET! FOR GROUP")
    print("MENU")
    print("--------------* MAIN TOOLS *----------------")
    print("1. Encode - Fully Converts a message to ENCODED numbers")
    print("2. Decode - Fully Decodes a set of ENCODED numbers to a message.")
    print()
    print("--------------* ADDITIONAL TOOLS *----------------")
    print("3. Partial Encode - Converts a message to numbers using ONLY lookup table. Does not run through encode function")
    print("4. Partial Decode - Converts UN-ENCODED numbers to a message using lookup table. Does not run through decode function")
    print("5. View Lookup Table")
    print("6. Exit")
    choice = input()

    if choice == "1":
        print("Enter your message to be encoded")
        message = input()
        encoded_array = Encode(message)
        print("Encoded message: ")
        print(*encoded_array, sep=' ')
        print("----------------------------------------------\n")
    elif choice == "2":
        decoded_message = Decode()
        print("Decoded message: ")
        print(decoded_message)
        print("----------------------------------------------\n")
    elif choice == "3":
        print("Enter your message to be converte to numbers using the simple lookup table. This does NOT encode the message with a function.")
        message = input()
        converted_array = PartialEncode(message)
        print("Message to lookup numbers: ")
        print(*converted_array, sep=' ')
        print("----------------------------------------------\n")
    elif choice == "4":
        converted_message = PartialDecode()
        print("Decoded message: ")
        print(converted_message)
        print("----------------------------------------------\n")
    elif choice == "5": 
        print("Lookup Table: ")
        print("-------------")
        for key, value in letter_dict.items():
            print(key, " : ", value)
        print("-------------")
        print("----------------------------------------------\n")
    elif choice == "6":
        print("Exiting")
        break
    else: 
        print("Invalid Choice")
        print("----------------------------------------------\n")

