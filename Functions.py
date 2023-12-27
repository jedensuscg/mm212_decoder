number_error = False
letter_error = False

def GetUnknownNumberError():
    global number_error
    return number_error

def GetUnknownLetterError():
    global letter_error
    return letter_error

def GetKeysFromValue(d, val):
    return [k for k, v in d.items() if v == val]

def CreateLookupTable():
    letter_dict = {}
    encoded_array = {}
    #Create index of letters
    for i in range(26):
        letter_dict[chr(ord('A') + i)] = i + 1
    letter_dict[' '] = 27
    return letter_dict

def Encode(message):
    global letter_error
    encoded_array = []
    for i in message:
        try:
            #Convert letter to Number
            number = LetterToNumberLookup(i)
            encoded_number = 5*number - 1
            encoded_array.append(encoded_number)
        except:
            letter_error = True
            encoded_array.append(0)
        else:
            letter_error = False
    return encoded_array

def PartialEncode(message):
    converted_array = []
    for i in message:
        #Convert letter to Number
        number = LetterToNumberLookup(i)
        #add to encrypted message
        converted_array.append(number)
    return converted_array

def Decode(message):
    global number_error
    encoded_array = message.split()
    decoded_message = ""
    for i in encoded_array:
        number = int(i)
        decoded_number = (number + 1)/5
        try:
            decoded_message += NumberToLetterLookup(decoded_number)
            number_error = False
        except:
            decoded_message += "?"
            number_error = True
        else:
            number_error = False
    return decoded_message

def PartialDecode(message):
    encoded_array = message.split()
    converted_message = ""
    for i in encoded_array:
        number = int(i)
        converted_message += NumberToLetterLookup(number)
    return converted_message

def NumberToLetterLookup(number):
    letter_dict = CreateLookupTable()
    if(number == type(int)):
        return "?"
    try:
        for key, value in letter_dict.items():
            if value == number:
                return key
            else:
                return "?"
    except:
        return "?"
        
def LetterToNumberLookup(letter):
    letter_dict = CreateLookupTable()
    if(letter == type(str)):
        return 0
    try:
        number = letter_dict[letter.upper()]
    except:
        return 0
    else:
        return number
    