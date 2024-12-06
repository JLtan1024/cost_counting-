import streamlit as st

# Title of the app
st.title("Repackaged Price Calculator with Unit Converter")

# Unit Converter Section
st.header("Unit Converter")

# Unit Conversion Options
conversion_type = st.radio("Choose Conversion Type:", ["Weight Conversion"])

# Output Container
conversion_result = ""

# Weight Conversion
if conversion_type == "Weight Conversion":
    weight_units = ["kg", "g", "lb", "oz"]
    input_weight_unit = st.selectbox("Convert From:", weight_units)
    output_weight_unit = st.selectbox("Convert To:", weight_units, index=1)
    input_weight = st.number_input(f"Enter Weight ({input_weight_unit}):", min_value=0.0, step=0.1)

    # Conversion Logic
    weight_in_grams = 0
    if input_weight_unit == "kg":
        weight_in_grams = input_weight * 1000
    elif input_weight_unit == "g":
        weight_in_grams = input_weight
    elif input_weight_unit == "lb":
        weight_in_grams = input_weight * 453.592
    elif input_weight_unit == "oz":
        weight_in_grams = input_weight * 28.3495

    converted_weight = 0
    if output_weight_unit == "kg":
        converted_weight = weight_in_grams / 1000
    elif output_weight_unit == "g":
        converted_weight = weight_in_grams
    elif output_weight_unit == "lb":
        converted_weight = weight_in_grams / 453.592
    elif output_weight_unit == "oz":
        converted_weight = weight_in_grams / 28.3495

    conversion_result = f"Converted Weight: {converted_weight:.2f} {output_weight_unit}"

# Display Conversion Result
if conversion_result:
    st.markdown("### Conversion Result")
    st.success(conversion_result)

# Divider
st.markdown("---")

# Repackaged Price Calculator Section
st.header("Repackaged Price Calculator")

# Input fields for bulk item details
weight_unit = st.selectbox("Select Weight Unit:", ["kg", "g", "lb", "oz"])
total_weight = st.number_input(f"Total Weight ({weight_unit}):", min_value=0.0, value=50.0, step=0.1)

# Total price in RM
total_price = st.number_input(f"Total Price (RM):", min_value=0.0, value=100.0, step=0.1)

# Convert weight to grams for uniform calculations
if weight_unit == "kg":
    total_weight_g = total_weight * 1000
elif weight_unit == "lb":
    total_weight_g = total_weight * 453.592
elif weight_unit == "oz":
    total_weight_g = total_weight * 28.3495
else:  # If weight is already in grams
    total_weight_g = total_weight

# Input options for repackaging
st.header("Repackaging Options")
repackaging_option = st.radio(
    "Choose the repackaging method:",
    ("By Weight per Pack", "By Number of Packs")
)

# Initialize results
num_packs = 0
price_per_pack = 0.0
weight_per_pack_g = 0.0

if repackaging_option == "By Weight per Pack":
    # User inputs weight per pack
    weight_per_pack_g = st.number_input("Weight per Pack (grams):", min_value=1.0, value=200.0, step=1.0)
    if weight_per_pack_g > 0:
        num_packs = total_weight_g / weight_per_pack_g
        price_per_pack = total_price / num_packs
else:
    # User inputs number of packs
    num_packs = st.number_input("Number of Packs:", min_value=1.0, value=250.0, step=1.0)
    if num_packs > 0:
        weight_per_pack_g = total_weight_g / num_packs
        price_per_pack = total_price / num_packs

# Display Results at the Bottom
st.markdown("### Repackaging Results")
st.write(f"**Total Weight:** {total_weight:.2f} {weight_unit} ({total_weight_g:.2f} grams)")
st.write(f"**Total Price:** {total_price:.2f} RM")
st.write(f"**Number of Packs:** {num_packs:.2f}")
st.write(f"**Weight per Pack:** {weight_per_pack_g:.2f} grams")
st.write(f"**Price per Pack:** {price_per_pack:.2f} RM")
