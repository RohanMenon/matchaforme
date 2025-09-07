import streamlit as st
import pandas as pd
import os

CSV_PATH = "matcha.csv"

st.title("Add a New Matcha Entry")

# Input fields
name = st.text_input("Matcha Name")
rating = st.number_input("Rating (0-10)", min_value=0.0, max_value=10.0, step=0.1)
price = st.number_input("Price (USD)", min_value=0.0, step=0.01, max_value=20.0, format="%.2f")

if st.button("Add Matcha"):
    if not name.strip():
        st.warning("Please enter a matcha name.")
    else:
        # Load existing data
        if os.path.exists(CSV_PATH):
            df = pd.read_csv(CSV_PATH)
        else:
            df = pd.DataFrame(columns=["name", "rating", "price"])
        # Append new row
        new_row = {"name": name.strip(), "rating": rating, "price": price}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        # Save back to CSV
        df.to_csv(CSV_PATH, index=False)
        st.success(f"Added: {name} (Rating: {rating}, Price: ${price:.2f})")
        st.dataframe(df.tail(5))
