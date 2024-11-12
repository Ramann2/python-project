import requests
import tkinter as tk
from tkinter import messagebox, Label, Frame, Canvas, Scrollbar
from PIL import Image, ImageTk
import io
from PIL.Image import Resampling

API_KEY = '65773cfbab93a4b947736543e8dd740c'

class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie App")
        self.root.geometry("800x600")

        self.search_frame = Frame(root)
        self.search_frame.pack(pady=10)

        self.search_label = Label(self.search_frame, text="Find a movie:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_movies)
        self.search_button.pack(side=tk.LEFT)

        self.results_frame = Frame(root)
        self.results_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.results_canvas = Canvas(self.results_frame)
        self.results_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_y = Scrollbar(self.results_frame, orient="vertical", command=self.results_canvas.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.results_canvas.configure(yscrollcommand=self.scrollbar_y.set)

        self.results_inner_frame = Frame(self.results_canvas)
        self.results_canvas.create_window((0, 0), window=self.results_inner_frame, anchor="nw")

        self.results_inner_frame.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))
        )

    def search_movies(self):
        query = self.search_entry.get().strip()
        if query:
            self.get_movies(query)
        else:
            messagebox.showerror("Error", "Please enter a movie name!")

    def get_movies(self, query):
        try:
            url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:

                for widget in self.results_inner_frame.winfo_children():
                    widget.destroy()

                if data['results']:
                    for movie in data['results']:
                        title = movie['title']
                        overview = movie.get('overview', 'No overview available.')
                        rating = movie.get('vote_average', 'No rating')
                        poster_path = movie.get('poster_path', '')

                        movie_frame = Frame(self.results_inner_frame, bg="white", padx=10, pady=10)
                        movie_frame.pack(fill=tk.X, pady=5)

                        if poster_path:
                            poster_url = f"https://image.tmdb.org/t/p/w200{poster_path}"
                            self.show_poster(poster_url, movie_frame)

                        Label(movie_frame, text=f"Title: {title}", font=("Arial", 14), anchor="w").pack(fill=tk.X)
                        Label(movie_frame, text=f"Overview: {overview}", anchor="w", wraplength=500).pack(fill=tk.X)
                        Label(movie_frame, text=f"Rating: {rating}", font=("Arial", 12), anchor="w").pack(fill=tk.X)

                else:
                    Label(self.results_inner_frame, text=f"No movies found for: {query}", font=("Arial", 14)).pack()

            else:
                messagebox.showerror("Error", "Failed to fetch data from TMDB.")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {str(e)}")

    def show_poster(self, poster_url, parent_frame):
        try:
            response = requests.get(poster_url)
            image = Image.open(io.BytesIO(response.content))
            image = image.resize((100, 150), Resampling.LANCZOS)
            img = ImageTk.PhotoImage(image)

            poster_label = tk.Label(parent_frame, image=img)
            poster_label.image = img
            poster_label.pack(side=tk.LEFT)
        except Exception as e:
            print(f"Error loading image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
