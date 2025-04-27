import streamlit as st
import requests
from utils import get_details, fetch_by_type

st.set_page_config(
    page_title="MoonFlix",
    page_icon="🎬",
)

st.sidebar.success("Welcome here you can search for your favorite movies/shows and put them in your watchlist/Liked movies.")

# intialize session state variables
if "watchlist" not in st.session_state:
    st.session_state.watchlist = {}
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "favorite_genres" not in st.session_state:
    st.session_state.favorite_genres = set()

st.title("🎬 MoonFlix 🎬")
st.subheader("Shoot for the Stars. Land a Perfect Movie.")
movie_query = st.text_input('Start typing a movie name...')

# condition to check if movie name was given
if movie_query:
    data = fetch_by_type(movie_query)

    if data['Response'] == "True":

        # Ask user how to sort
        sort_by = st.selectbox("Sort by", ["IMDb Rating", "Title A-Z", "Year"])
        
        movies = sorted(
            data['Search'],
            key=lambda movie: (
                float(get_details(movie['imdbID']).get("imdbRating", 0)) if sort_by == "IMDb Rating" else
                get_details(movie['imdbID']).get("Title", "") if sort_by == "Title A-Z" else
                get_details(movie['imdbID']).get("Year", "")
            ),
            reverse=(sort_by in ["IMDb Rating", "Year"])
        )

        for movie in movies:
            details = get_details(movie['imdbID'])

            title = details.get("Title", "No title found")
            poster = details.get("Poster", "")
            rating = details.get("imdbRating", "N/A")
            genres = details.get("Genre", "Unknown genre").split(',')
            plot = details.get("Plot", "No description available.")

            st.subheader(title)
            if poster != "N/A" and poster.strip() != "":
                st.image(poster,use_container_width=True)
            else:
                st.info("🎞️ Poster not available.")

            st.write(f"Year: {details['Year']}")
            st.write(f"⭐ Rating: {details['imdbRating']}")
            st.write(f"Genre: {details['Genre']}")
            st.write(f"Plot: {details['Plot']}")

            favorite_clicked = st.button("Add to favorite", type="primary", key=movie['imdbID'])
            if favorite_clicked:
                st.session_state.watchlist[movie['imdbID']] = details
                for genre in genres:
                    st.session_state.favorite_genres.add(genre.lower())

            st.markdown("-----")
    else:
        st.error('Movie not found...🥲🥲')