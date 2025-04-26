Movie Recommendation
# OMDb Streamlit App

A multi-page Streamlit application that allows you to search movies and series from the OMDb API, add them to your watchlist, rate them, and get personalized recommendations based on your favorite genres!

## Features

- *Movie/Series Search*: Search for any movie or TV show by name. View detailed information like poster, year, IMDb rating, genres, and plot.
- *Sorting*: Sort search results by IMDb Rating, Title (A-Z), or Year.
- *Watchlist*: Save your favorite movies/shows to your personal watchlist. Rate them and mark them as watched.
- *Recommendations*: Get smart recommendations based on genres you like the most (automatically learned from your watchlist).
- *Session Persistence*: Your data (watchlist, ratings, genres) persists during your session with the app.

## Project Structure


```plaintext
.
├── 0_Home.py              # Home page: Search movies/shows and add to watchlist
├── 1_Watchlist.py         # Watchlist page: View, rate, and manage your saved movies
├── 2_Recommendations.py   # Recommendations page: Get movie suggestions
├── .env                   # Store your OMDb API Key
├── requirements.txt       # List of Python packages required
└── README.txt             # This file
```


## Installation

1. *Clone the repository*:

bash
git clone https://github.com/MajedAlsarwani/Movies-Recommendation.git
cd Movies-Recommendation



2. *Install the required packages*:

bash
pip install -r requirements.txt


3. *Get your OMDb API Key*:
   Sign up for a free API key at https://www.omdbapi.com/apikey.aspx.

4. **Create a .env file**:

Inside the project directory, create a .env file and add your API key:


API_KEY=your_omdb_api_key_here


## Running the App

bash
streamlit run 0_Home.py


- Use the sidebar to navigate between Home, Watchlist, and Recommendations pages.

## Requirements

- Python 3.7+
- Streamlit
- Requests
- Python-dotenv

(Already listed inside requirements.txt.)

## Screenshots

## 🎬 Home Page
![Image](https://github.com/user-attachments/assets/a6b166bb-4340-4486-8a98-a12c44280bf3)
## 📋 Watchlist Page
![Image](https://github.com/user-attachments/assets/58965073-b83d-4904-8824-38707811f745)
## 🌟 Recommendations
![Image](https://github.com/user-attachments/assets/0d6ae007-1c5e-435f-a0a4-1b47ded3255b)

## Notes

- Recommendations are fetched using random common keywords and matched against your liked genres.
- It gracefully handles missing posters, ratings, or genre data.

## License

This project is open-source and free to use.
