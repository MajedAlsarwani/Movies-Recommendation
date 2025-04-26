import streamlit as st
from utils import get_details, fetch_all_pages 

st.info("Auto-recommendations based on your favorite genres!")

content_type = st.radio("Select content type:", ["movie", "series"], horizontal=True)
sort_by = st.selectbox("Sort by", ["IMDb Rating", "Title A-Z", "Year"])

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
        movies = sorted(
                filtered_movies,
                key=lambda movie: (
                    float(movie.get("imdbRating", 0)) if sort_by == "IMDb Rating" else
                    movie.get("Title", "") if sort_by == "Title A-Z" else
                    movie.get("Year", "")
                ),
                reverse=(sort_by in ["IMDb Rating", "Year"])
            )
        for movie in movies:  
            st.subheader(movie.get("Title"))
            st.image(movie.get("Poster"), use_container_width=True)
            st.write(f"Year: {movie.get('Year')}")
            st.write(f"Rating: {movie.get('imdbRating')}")
            st.write(f"Genre: {movie.get('Genre')}")
            st.caption(movie.get("Plot"))
    else:
        st.warning("No movies match your favorite genres.")
else:
    st.error("Failed to fetch movies. Please try again.")
 