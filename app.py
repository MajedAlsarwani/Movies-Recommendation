import streamlit as st
import requests

# import api key from .env file
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

# function to return a search list of movies

@st.cache_data
def fetch_movie(query):
    url = f'http://www.omdbapi.com/?i=tt3896198&apikey={api_key}&s={query}'
    response = requests.get(url)
    return response.json()

# function to return deatils of movies
def get_movie_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
    response = requests.get(url)
    return response.json()


st.title("🎬 Movie Search with OMDb API")

movie_query = st.text_input('Start typing a movie name...')

# condition to check if movie name was given
if movie_query:
    data = fetch_movie(movie_query)

    # condition to check if data was found 
    if data['Response'] == "True":

        # looping through the movies to take id and get details
        for movie in data['Search']:
            details = get_movie_details(movie['imdbID'])

          # handling errors if missing values  
            title = details.get("Title", "No title found")
            poster = details.get("Poster", "")
            rating = details.get("imdbRating", "N/A")
            genre = details.get("Genre", "Unknown genre")
            plot = details.get("Plot", "No description available.")

            # showing list of movies found
            st.subheader(details['Title'])
            if poster != "N/A" and poster.strip() != "":
                st.image(poster)
            else:
                st.info("🎞️ Poster not available.")
            
            st.write(f' Year: {details['Year']}')
            st.write(f'⭐ Rating: {details['imdbRating']}')
            st.write(f' Genre: {details['Genre']}')
            st.write(f' Plot: {details['Plot']}')
            st.markdown("-----")
            
    else:
        st.error('Movie not found...🥲🥲')

