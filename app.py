import streamlit as st
import requests

st.set_page_config(
    page_title="Movie Search",
    page_icon="🎬",
)

st.sidebar.success("Welcome here you can search for your favorite movies/shows and put them in your watchlist/Liked movies.")
favorite_genre = set()
# import api key from .env file
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
if "watchlist" not in st.session_state:
    st.session_state.watchlist = {}
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "favorite_genres" not in st.session_state:
    st.session_state.favorite_genres = set()
# function to return a search list of movies

@st.cache_data
def fetch_movie(query):
    url = f'http://www.omdbapi.com/?i=tt3896198&apikey={api_key}&s={query}'
    response = requests.get(url)
    return response.json()

# function to return details of movies
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
            genre = details.get("Genre", "Unknown genre").split(',')
            plot = details.get("Plot", "No description available.")
            # imdbid = details.get("imdbID", "No description available.")
          
            
            # showing list of movies found
            st.subheader(details['Title'])
            if poster != "N/A" and poster.strip() != "":
                st.image(poster)
            else:
                st.info("🎞️ Poster not available.")

            st.write(f" Year: {details['Year']}")
            st.write(f"⭐ Rating: {details['imdbRating']}")
            st.write(f" Genre: {details['Genre']}")
            st.write(f" Plot: {details['Plot']}")
            favorite_clicked = st.button("Add to favorite", type="primary",key = movie['imdbID'])
            if favorite_clicked:
                  
                    st.session_state.watchlist[ movie['imdbID']] = details
                    for g in genre:
                        st.session_state.favorite_genres.add(g.lower())

                
            st.markdown("-----")
            st.write(f'your favorite genres {st.session_state.favorite_genres}')

            
            
    else:
        st.error('Movie not found...🥲🥲')