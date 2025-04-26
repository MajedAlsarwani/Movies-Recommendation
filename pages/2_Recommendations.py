import streamlit as st
from utils import get_details, fetch_all_pages 

# load_dotenv()
# api_key = os.getenv("API_KEY")

# def get_details(imdb_id):
#     url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
#     return requests.get(url).json()

# def fetch_by_type(content_type, page=1):
#     """Fetch movies or shows by type with pagination."""
#     url = f"http://www.omdbapi.com/?apikey={api_key}&s={content_type}&page={page}"
#     return requests.get(url).json()

# def fetch_all_pages(content_type, max_pages=5):
#     """Fetch multiple pages of results."""
#     all_results = []
#     for page in range(1, max_pages + 1):
#         data = fetch_by_type(content_type, page)
#         if data.get("Response") == "True":
#             all_results.extend(data["Search"])
#         else:
#             break
#     return all_results


st.info("Auto-recommendations based on your favorite genres!")

content_type = st.radio("Select content type:", ["movie", "series"], horizontal=True)

favorite_genres = list(st.session_state.favorite_genres)


if not favorite_genres:
    st.warning("Add movies to your watchlist to build your favorite genres.")
else:
    st.write(f"Your favorite genres: {', '.join(favorite_genres)}")
   

# Fetch movies by type and store them in a variable
fetched_movies = fetch_all_pages(content_type)

if fetched_movies:
    filtered_movies = []
    for item in fetched_movies:
        imdb_id = item["imdbID"]
        details = get_details(imdb_id)

        if details.get("Genre"):
            genres = set(g.strip().lower() for g in details.get("Genre", "").split(","))
            matched = st.session_state.favorite_genres & genres

            if matched:
                filtered_movies.append(details)

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
 