from sympy import *
x = symbols('x')
number_error = False
letter_error = False
encode_expression = sympify("5*x-1")
decode_expression = sympify("(x+1)/5")

def SetEncodeExpression(exp):
    global encode_expression
    encode_expression = sympify(exp)

def GetEncodeExpression():
    global encode_expression
    return encode_expression

def GetDecodeExpression():
    global decode_expression
    return decode_expression

def SetDecodeExpression(exp):
    global decode_expression
    decode_expression = sympify(exp)

def GetUnknownNumberError():
    global number_error
    return number_error

def GetLatexExpression(exp):
    return latex(exp)

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
            encoded_number = encode_expression.subs(x, number)
            encoded_array.append(encoded_number)

        except Exception as e:
            print(e)
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
        try:
            number = int(i)
        except:
            number = 0
        decoded_number = decode_expression.subs(x, number) 
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
        try:
            converted_message += NumberToLetterLookup(number)
        except:
            converted_message += "?"
            number_error = True
        else:
            number_error = False
    return converted_message

def NumberToLetterLookup(number):
    letter_dict = CreateLookupTable()
    try:
        for key, value in letter_dict.items():
            if value == number:
                return key
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
    