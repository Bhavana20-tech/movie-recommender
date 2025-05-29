import streamlit as st
import requests

# Your OMDB API key
API_KEY = '66fee098'

# Dummy list of recommended movies (replace with your actual logic)
def recommend(movie):
    return ['Aliens', 'Moonraker', 'Alien', 'Alien³', 'Silent Running', 'Gravity', 'Interstellar', 'The Martian']

# Fetch movie poster using OMDB API
def fetch_poster(movie_name, api_key=API_KEY):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['Response'] == 'True' and data['Poster'] != 'N/A':
        return data['Poster']
    else:
        return "https://via.placeholder.com/150?text=No+Image"

# Streamlit UI
st.title("🎬 Movie Recommender System")

movie_name = st.text_input("Enter a movie name", key="movie_input")

if st.button("Recommend"):
    recommended_movies = recommend(movie_name)
    st.subheader("Recommended Movies:")

    # Display in a 4-column grid
    for i in range(0, len(recommended_movies), 4):
        row = st.columns(4)
        for j in range(4):
            if i + j < len(recommended_movies):
                movie = recommended_movies[i + j]
                poster_url = fetch_poster(movie)
                with row[j]:
                    st.image(poster_url, width=150)
                    st.caption(movie)
