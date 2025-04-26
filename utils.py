import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")


def fetch_movie(query):
    url = f'http://www.omdbapi.com/?i=tt3896198&apikey={api_key}&s={query}'
    response = requests.get(url)
    return response.json()

def get_details(imdb_id):
    """Fetch detailed information about a movie or show."""
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
    return requests.get(url).json()

def fetch_by_type(content_type, page=1):
    """Fetch movies or shows by type with pagination."""
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={content_type}&page={page}"
    return requests.get(url).json()

def fetch_all_pages(content_type, max_pages=5):
    """Fetch multiple pages of results."""
    all_results = []
    for page in range(1, max_pages + 1):
        data = fetch_by_type(content_type, page)
        if data.get("Response") == "True":
            all_results.extend(data["Search"])
        else:
            break
    return all_results