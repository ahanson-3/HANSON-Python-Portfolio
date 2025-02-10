import streamlit as st

import pandas as pd

st.title("Welcome to Penguin Data!")

st.subheader("On this streamlit app you can view data on the Palmer penguins of the Antartic Archipelego.")

if st.button("Click me!🐧"):
    st.write("You clicked the button! Nice work!🌨️")
else:
    st.write("Click the button to see what happens...")

df = pd.read_csv("basic_streamlit-app/data/penguins.csv")

# Displaying the table in Streamlit
# st.dataframe() makes it interactive (sortable, scrollable)
st.write("Here's a table of all the data. Scroll further to filter by species:")
st.dataframe(df)

species = st.selectbox("Select a species", df["species"].unique())

# Create a filtered DataFrame that only includes rows matching the selected city.
filtered_df = df[df["species"] == species]

# Display the filtered results with an appropriate heading.
st.write(f"Penguins of the {species} species:")
st.dataframe(filtered_df)  # Show the filtered table

island = st.selectbox("Select a island", df["island"].unique())

# Create a filtered DataFrame that only includes rows matching the selected city.
filtered_df = df[df["island"] == island]

# Display the filtered results with an appropriate heading.
st.write(f"Penguins of the {island} island:")
st.dataframe(filtered_df)  # Show the filtered table