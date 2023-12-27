#f(x) = 5x - 1
import streamlit as st
import pandas as pd
from Functions import Encode, PartialEncode, Decode, PartialDecode, CreateLookupTable, GetKeysFromValue, GetUnknownNumberError, GetUnknownLetterError
st.set_page_config(layout="wide")
st.header("SECRET DECODER TOOL - TOP SECRET - FOR MM212 USE ONLY")
tab1, tab2, tab3 = st.tabs(["Encode", "Decode", "Lookup Table"])

with tab1:
    with st.expander("FULL ENCODE", False):
        st.write("This tool will take a message and convert it to numbers using the special encoding function")
        st.write("Enter your message to be encoded")
        message = st.text_input("message to encode")
        encoded_array = Encode(message)
        st.write("Encoded message: ")
        encoded_message = ""
        for i in encoded_array:
            encoded_message += f'{i} '
        st.write(encoded_message)
        if(GetUnknownLetterError()):
           st.write("NOTE: Some characters could not be encoded due to input error. They have been replaced with a '0'")

    with st.expander("PARTIAL ENCODE", False):
        st.write("This tool will take a message and convert it to numbers using ONLY the lookup table. \n NOTE: It does NOT run through the encode function.")
        st.write("Enter your message to be converted.")
        message = st.text_input("Message to convert.")
        converted_array = PartialEncode(message)
        st.write("Message to lookup numbers: ")
        df = pd.DataFrame()
        letter_dict = CreateLookupTable()
        count = 0
        for i in converted_array:
            df.insert(count,count,(i ,GetKeysFromValue(letter_dict, i)[0]),True)
            count += 1
        df.index=["LETTER","NUMBER"]
        st.dataframe(df,hide_index=True)

with tab2:
    with st.expander("FULL DECODE", False):
        st.write("This tool will take a message and convert it to numbers using the following function:")
        st.write("Enter each number of your message to be decoded, separated by a space: i.e 45 10 1")
        message = st.text_input("Message to Decode")
        decoded_message = Decode(message)
        st.write("Decoded message: ")
        st.write(decoded_message)
        if(GetUnknownNumberError()):
            st.write("NOTE: Some characters could not be decoded. They have been replaced with a '?'")
    with st.expander("PARTIAL DECODE", False):
        st.write("This tool will take a message and convert it to numbers using ONLY the lookup table. It does not run through the decode function.")
        st.write("Enter your each number to be converted, separated by a space (1-27)")
        message = st.text_input("Numbers to convert to text.")
        converted_message = PartialDecode(message)
        st.write("Decoded message: ")
        st.write(converted_message)

with tab3:
    st.write("Lookup Table: ")
    st.write("-------------")
    df = pd.DataFrame()
    letter_dict = CreateLookupTable()
    count = 0
    for i in letter_dict:
        df.insert(count,count,(i ,letter_dict[i]),True)
        count += 1
    df.index=["LETTER","NUMBER"]
    st.dataframe(df,hide_index=True)
