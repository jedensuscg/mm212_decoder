#f(x) = 5x - 1
import streamlit as st
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
    st.write("Enter each number of the encoded message, seperated by a space: i.e 45 10 1")
    encoded_message = st.text()
    encoded_array = encoded_message.split()
    decoded_message = ""
    for i in encoded_array:
        number = int(i)
        decoded_number = (number + 1)/5
        decoded_message += NumberToLetterLookup(decoded_number)
    return decoded_message

def PartialDecode():
    encoded_message = st.text_input()()
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
    st.write("         ** MM212 SECRET DECODER TOOL **")
    st.write("         TOP SECRET! FOR GROUP")
    st.write("MENU")
    st.write("--------------* MAIN TOOLS *----------------")
    st.write("1. Encode - Fully Converts a message to ENCODED numbers")
    st.write("2. Decode - Fully Decodes a set of ENCODED numbers to a message.")
    st.write()
    st.write("--------------* ADDITIONAL TOOLS *----------------")
    st.write("3. Partial Encode - Converts a message to numbers using ONLY lookup table. Does not run through encode function")
    st.write("4. Partial Decode - Converts UN-ENCODED numbers to a message using lookup table. Does not run through decode function")
    st.write("5. View Lookup Table")
    st.write("6. Exit")
    choice = st.text_input()()

    if choice == "1":
        st.write("Enter your message to be encoded")
        message = st.text_input()()
        encoded_array = Encode(message)
        st.write("Encoded message: ")
        st.write(*encoded_array, sep=' ')
        st.write("----------------------------------------------\n")
    elif choice == "2":
        decoded_message = Decode()
        st.write("Decoded message: ")
        st.write(decoded_message)
        st.write("----------------------------------------------\n")
    elif choice == "3":
        st.write("Enter your message to be converte to numbers using the simple lookup table. This does NOT encode the message with a function.")
        message = st.text_input()()
        converted_array = PartialEncode(message)
        st.write("Message to lookup numbers: ")
        st.write(*converted_array, sep=' ')
        st.write("----------------------------------------------\n")
    elif choice == "4":
        converted_message = PartialDecode()
        st.write("Decoded message: ")
        st.write(converted_message)
        st.write("----------------------------------------------\n")
    elif choice == "5": 
        st.write("Lookup Table: ")
        st.write("-------------")
        for key, value in letter_dict.items():
            st.write(key, " : ", value)
        st.write("-------------")
        st.write("----------------------------------------------\n")
    elif choice == "6":
        st.write("Exiting")
        break
    else: 
        st.write("Invalid Choice")
        st.write("----------------------------------------------\n")

