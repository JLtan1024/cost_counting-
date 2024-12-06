import streamlit as st

# Title of the app
st.title("Repackaged Price Calculator")

# Input fields for bulk item details
st.header("Bulk Item Details")
total_weight_kg = st.number_input("Total Weight (kg)", min_value=0.0, value=50.0, step=0.1)
total_price = st.number_input("Total Price (in currency)", min_value=0.0, value=100.0, step=0.1)

# Convert total weight to grams
total_weight_g = total_weight_kg * 1000

# Input options for repackaging
st.header("Repackaging Options")
repackaging_option = st.radio(
    "Choose the repackaging method:",
    ("By Weight per Pack", "By Number of Packs")
)

if repackaging_option == "By Weight per Pack":
    weight_per_pack_g = st.number_input(
        "Weight per Pack (grams)", min_value=1.0, value=200.0, step=1.0
    )
    if weight_per_pack_g > 0:
        num_packs = total_weight_g / weight_per_pack_g
        price_per_pack = total_price / num_packs
        st.write(f"Number of Packs: {num_packs:.2f}")
        st.write(f"Price per Pack: {price_per_pack:.2f} currency units")
    else:
        st.error("Weight per pack must be greater than 0.")
else:
    num_packs = st.number_input("Number of Packs", min_value=1.0, value=250.0, step=1.0)
    if num_packs > 0:
        weight_per_pack_g = total_weight_g / num_packs
        price_per_pack = total_price / num_packs
        st.write(f"Weight per Pack: {weight_per_pack_g:.2f} grams")
        st.write(f"Price per Pack: {price_per_pack:.2f} currency units")
    else:
        st.error("Number of packs must be greater than 0.")

# Footer
st.write("This tool helps calculate the price and weight per pack for repackaging purposes.")
