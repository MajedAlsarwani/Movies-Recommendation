import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

if "watchlist" not in st.session_state:
    st.session_state.watchlist = {}
if "watchlist_dict" not in st.session_state:
    st.session_state.watchlist_dict = {}
if "favorite_genres" not in st.session_state:
    st.session_state.favorite_genres = set()

def get_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
    return requests.get(url).json()

def fetch_by_type(content_type):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={content_type}"
    return requests.get(url).json()


st.info("Auto-recommendations based on your favorite genres!")

content_type = st.radio("Select content type:", ["movie", "series"], horizontal=True)

favorite_genres = list(st.session_state.favorite_genres)


if not favorite_genres:
    st.warning("Add movies to your watchlist to build your favorite genres.")
else:
    count = 0
   

# Fetch movies by type and store them in a variable
data = fetch_by_type(content_type)

if data.get("Response") == "True":
    fetched_movies = data["Search"]  # Store all fetched movies
    filtered_movies = []  # To store movies matching favorite genres

    for item in fetched_movies:
        imdb_id = item["imdbID"]
        details = get_details(imdb_id)

        if details.get("Genre"):
            genres = set(g.strip().lower() for g in details.get("Genre", "").split(","))
            matched = st.session_state.favorite_genres & genres

            if matched:  # If there is a match
                filtered_movies.append(details)  # Store the movie in the filtered list

    # Display the filtered movies
   
    if filtered_movies:
        
        for movie in filtered_movies:
            st.subheader(movie.get("Title"))
            st.image(movie.get("Poster"), use_column_width=True)
            st.write(f"Year: {movie.get('Year')}")
            st.write(f"Rating: {movie.get('imdbRating')}")
            st.write(f"Genre: {movie.get('Genre')}")
            st.caption(movie.get("Plot"))

    else:
        st.warning("No movies match your favorite genres.")
else:
    st.error("Failed to fetch movies. Please try again.")
 