import streamlit as st

st.set_page_config(
    page_title="🎥 Your Watchlist", 
    page_icon="📋")

st.title("Your Watchlist")

if not st.session_state.watchlist:
    
    st.info("Your watchlist is empty.")


if "watchlist" not in st.session_state:
    st.session_state.watchlist = {}
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "favorite_genres" not in st.session_state:
    st.session_state.favorite_genres = set()



for imdb_id, movie in st.session_state.watchlist.items():
    st.subheader(movie.get("Title"))
    st.image(movie.get("Poster"), use_column_width=True)

    user_rating = st.slider(f"Your Rating for {movie.get('Title')}", 0, 10, st.session_state.user_data.get(imdb_id, {}).get("rating", 0))
    watched = st.checkbox(f"Mark as Watched: {movie.get('Title')}", value=st.session_state.user_data.get(imdb_id, {}).get("watched", False))

    

    if st.button(f"Remove {movie.get('Title')} from Watchlist"):
        st.session_state.watchlist = [m for m in st.session_state.watchlist if m.get("imdbID") != imdb_id]
        st.session_state.watchlist_dict.pop(imdb_id, None)
        st.session_state.user_data.pop(imdb_id, None)
        # st.write(st.session_state.watchlist)
        #  st.subheader(movie['Title'])
        # 
         
         




        #st.write(f'your movie is: {index['Title']}')
        #st.write(f'your movie Year is: {index['Year']}')
    # st.write(st.session_state.watchlist)
    # st.write(st.session_state.watchlist)
    # st.write(st.session_state.watchlist)
    # st.subheader(movie['title'])
    # if movie['Poster'] != "N/A":
    #     st.image(movie["Poster"])
    #     st.write(f"Year: {movie['Year']}")
    #     st.write(f"Rating: {movie['imdbRating']}")
    #     st.write(f"Genre: {movie['Genre']}")
    #     st.write(f"Plot: {movie['Plot']}")
    #     st.markdown("----")
    # else:
    #     st.info("🕵️ Your watchlist is empty. Go add some movies!")
