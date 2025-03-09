import streamlit as st
from pint import UnitRegistry

# Initialize Pint
ureg = UnitRegistry()

# Define unit categories with correct unit names
unit_defaults = {
    "Area": ("square meter", "square foot", 1.0),  # ✅ Fixed spacing issue
    "Data Transfer Rate": ("bit / second", "kilobit / second", 1.0),  
    "Digital Storage": ("byte", "kilobyte", 1.0),  
    "Energy": ("joule", "calorie", 1.0),  
    "Frequency": ("hertz", "kilohertz", 1.0),  
    "Fuel Economy": ("kilometer / liter", "mile / gallon", 1.0),  
    "Length": ("meter", "centimeter", 1.0),  
    "Mass": ("kilogram", "gram", 1.0),  
    "Plane Angle": ("degree", "radian", 1.0),  
    "Pressure": ("pascal", "bar", 1.0),  
    "Speed": ("meter / second", "kilometer / hour", 1.0),  
    "Time": ("second", "minute", 1.0),  
    "Volume": ("liter", "milliliter", 1.0)  
}

# Streamlit UI
st.title("Unit Converter")

# Dropdown for selecting unit category
unit_category = st.selectbox("Select Unit Category", list(unit_defaults.keys()), index=6)  # Default: Length

# Get default units and value
default_from_unit, default_to_unit, default_value = unit_defaults[unit_category]

# Get valid units for the selected category
compatible_units = ureg.get_compatible_units(default_from_unit)
valid_units = sorted([str(unit) for unit in compatible_units])

# Ensure default units exist in the list
if default_from_unit not in valid_units:
    valid_units.insert(0, default_from_unit)
if default_to_unit not in valid_units:
    valid_units.append(default_to_unit)

# Dropdowns for "Convert from" and "Convert to"
from_unit = st.selectbox("Convert from", valid_units, index=valid_units.index(default_from_unit))
to_unit = st.selectbox("Convert to", valid_units, index=valid_units.index(default_to_unit))

# Number input for value
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f", value=float(default_value))

# Perform conversion
if st.button("Convert"):
    try:
        converted_value = (value * ureg(from_unit)).to(to_unit).magnitude
        st.success(f"Converted value of {value} {from_unit} = {converted_value:.2f} {to_unit}")
    except Exception as e:
        st.error(f"⚠️ Conversion not supported: {e}")