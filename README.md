Movie App 🎬

This is a simple GUI-based movie search application built with Python's Tkinter library. The app allows users to search for movies and displays details such as title, overview, rating, and movie poster, fetched from an external API.

Features

Search for Movies: Users can enter a movie title and get search results.

Display Movie Details: Shows each movie's title, overview, rating, and poster.

Scrollable Results: Displays a scrollable list of search results.


Installation

Prerequisites

Python 3.x is required.

Install required libraries:

pip install requests pillow


Setup

1. Clone the repository or copy the code into a Python file.


2. Run the application:

python main.py



Usage

1. Enter the name of a movie in the search box.


2. Click the Search button to display results.


3. The app will display each movie's title, overview, rating, and poster if available.



Code Overview

MovieApp Class: Initializes the main GUI structure and handles movie search and display functionality.

search_movies: Retrieves the movie title from the input field and initiates the search.

get_movies: Fetches movie data from the external API based on the search query.

show_poster: Loads and displays each movie's poster.
