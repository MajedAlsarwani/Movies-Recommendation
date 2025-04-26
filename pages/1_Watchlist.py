import streamlit as st

st.set_page_config(
    page_title="🎥 Your Watchlist", 
    page_icon="📋")

st.title("Your Watchlist")

if not st.session_state.watchlist:
    st.info("Your watchlist is empty.😅😅")


movie_to_remove = None

for imdb_id in list(st.session_state.watchlist.keys()):
    movie = st.session_state.watchlist[imdb_id]
    st.subheader(movie.get("Title"))

    user_data = st.session_state.user_data.get(imdb_id, {})
    user_rating = user_data.get("rating", 0)
    watched = user_data.get("watched", False)

    if user_rating > 0:
        st.write(f"⭐ Your Rating: {user_rating}/10")
    if watched:
        st.write("✅ Marked as Watched")

    st.image(movie.get("Poster"),use_container_width=True)

    new_rating = st.slider(f"Your Rating for {movie.get('Title')}", 0, 10, user_rating)
    new_watched = st.checkbox(f"Mark as Watched: {movie.get('Title')}", value=watched)

    if new_rating != user_rating or new_watched != watched:
        st.session_state.user_data[imdb_id] = {"rating": new_rating, "watched": new_watched}
        st.rerun()

    if st.button(f"Remove {movie.get('Title')} from Watchlist", key=f"remove_{imdb_id}"):
        movie_to_remove = imdb_id

if movie_to_remove:
    removed_movie = st.session_state.watchlist.pop(movie_to_remove, None)
    st.session_state.user_data.pop(movie_to_remove, None)

# Recalculate favorite genres dynamically based on the current watchlist
    all_genres = set()
    for movie in st.session_state.watchlist.values():
        movie_genres = set(g.strip().lower() for g in movie.get("Genre", "").split(","))
        all_genres.update(movie_genres)

    st.session_state.favorite_genres = all_genres


    st.rerun()
