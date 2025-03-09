import streamlit as st # streamlit is a library for building web apps

#function to converts units based on predefined conversion factors or formula
def convert_units(value, unit_from,unit_to):
    
    conversions={
        "meter_kilometer":0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter":1000, # 1 kilometer = 1000 meter
        "gram_kilogram":0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram":1000 # 1 ilogram = 1000 gram
    }
    key=f"{unit_from}_{unit_to}" # generate a key based on the input and output units
    # logic to convert units
    if key in conversions:
        conversion=conversions[key]
        return value*conversion
    else:
        return "Conversion not supported" # return a message if the conversion is not supported
    
st.title("Unit Converter") # set the title of the web app

# user input: numerical value to convert
value=st.number_input("Enter the value:",min_value=1.0,step=1.0)

# dropdown to select unit to convert from
unit_from=st.selectbox("Convert from:",["meter","kilometer","gram","kilogram"])

# dropdown to select unit to convert to 
unit_to=st.selectbox("Cnvert to:",["meter","kilometer","gram","kilogram"])

# button to trigger the conversion
if st.button("Convert"):
    result =convert_units(value,unit_from,unit_to) # call the conversion function
    st.write(f"Converted value: {result}") # display the result