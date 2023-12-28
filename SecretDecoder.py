
from Functions import Encode, PartialEncode, Decode, PartialDecode, CreateLookupTable, GetUnknownNumberError, GetUnknownLetterError, SetEncodeExpression, GetEncodeExpression
SetEncodeExpression()

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
        if(GetUnknownLetterError()):
            print("NOTE: Some characters could not be encoded due to invalid input. They have been replaced with a '0'")
        print("Press Enter To Continue")
        input()
        print("----------------------------------------------\n")
    elif choice == "2":
        print("Enter each number of the encoded message, seperated by a space: i.e 45 10 1")
        message = input()
        decoded_message = Decode(message)
        print("Decoded message: ")
        print(decoded_message)
        if(GetUnknownNumberError()):
            print("NOTE: Some characters could not be decoded. They have been replaced with a '?'")
        print("Press Enter To Continue")
        input()
        print("----------------------------------------------\n")
    elif choice == "3":
        print("Enter your message to be converted to numbers using the simple lookup table. This does NOT encode the message with a function.")
        message = input()
        converted_array = PartialEncode(message)
        print("Message to lookup numbers: ")
        print(*converted_array, sep=' ')
        print("Press Enter To Continue")
        input()
        print("----------------------------------------------\n")
    elif choice == "4":
        print("Enter each number of the message, separated by a space (1-27)");
        converted_message = PartialDecode(message)
        print("Converted message: ")
        print(converted_message)
        print("Press Enter To Continue")
        input()
        print("----------------------------------------------\n")
    elif choice == "5": 
        print("Lookup Table: ")
        print("-------------")
        for key, value in CreateLookupTable().items():
            print(key, " : ", value)
        print("-------------")
        print("----------------------------------------------\n")
    elif choice == "6":
        print("Exiting")
        break
    else: 
        print("Invalid Choice")
        print("----------------------------------------------\n")

