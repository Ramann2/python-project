# Movie App 🎬

This is a simple GUI-based movie search application built with Python's Tkinter library. The app interacts with the TMDB (The Movie Database) API to allow users to search for movies, displaying details such as title, overview, rating, and movie poster.

## Features

- **Search for Movies**: Users can enter a movie title and get search results from the TMDB API.
- **Display Movie Details**: Shows each movie's title, overview, rating, and poster.
- **Scrollable Results**: Displays a scrollable list of search results.

## Installation

### Prerequisites

- **Python 3.x** is required.
- **Install required libraries**:
  ```bash
  pip install requests pillow
  ```

### Setup

1. Clone the repository or copy the code into a Python file.
2. Obtain an API key from [TMDB](https://www.themoviedb.org/) and replace `API_KEY` in the code with your key.
3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Enter the name of a movie in the search box.
2. Click the **Search** button to display results.
3. The app will display each movie's title, overview, rating, and poster if available.

## Code Overview

- **`MovieApp` Class**: Initializes the main GUI structure and handles movie search and display functionality.
  - **`search_movies`**: Retrieves the movie title from the input field and initiates the search.
  - **`get_movies`**: Fetches movie data from the TMDB API based on the search query.
  - **`show_poster`**: Loads and displays each movie's poster.

## TMDB API Key

Replace `API_KEY` in the script with your own TMDB API key.
