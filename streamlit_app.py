import streamlit as st

st.title("Movie Recommender")

movie = st.text_input("Enter a movie name")

if st.button("Recommend"):
    st.write(f"Recommendations for '{movie}' will appear here.")
