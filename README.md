🎬 Movie Project — SQLite + OMDb API + HTML Website

A Python application that lets you manage your personal movie database, fetch real movie data from the OMDb API, store it locally in an SQLite database, and even generate a styled website displaying your movie collection.

🚀 Features

Add movies automatically from OMDb
→ Just type a title — the app fetches the movie’s year, rating, and poster URL.

Store movies locally using SQLite
→ Persistent storage using SQLAlchemy.

Manage your collection
→ List, delete, search, update ratings, and view stats.

Generate a custom website
→ Builds an index.html file using your template and CSS to show all posters and details.

Error handling
→ Handles missing movies, API errors, and invalid input gracefully.

🛠️ Technologies Used

Python 3

SQLite (via SQLAlchemy)

OMDb API – https://www.omdbapi.com/

HTML / CSS (static website generation)

📦 Project Structure
MovieProjectSQLiteAPIHTML/
│
├── movies.py                # Main CLI application
├── movie_storage_sql.py     # SQLite database handler (SQLAlchemy)
├── data_fetcher.py          # Fetches movie data from OMDb API
│
├── template.html            # HTML template for website generation
├── style.css                # Stylesheet for generated website
│
├── .env                     # Contains your OMDb API key
├── movies.db                # SQLite database (auto-generated)
└── README.md



⚙️ Setup & Installation

Clone the repository

git clone https://github.com/PatrickIOb/Movie-Project-API-HTML-SQL.git
cd Movie-Project-API-HTML-SQL


Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate      # on macOS/Linux
.venv\Scripts\activate         # on Windows


Install dependencies

pip install sqlalchemy requests python-dotenv


Create a .env file in the project root and add your OMDb API key:

API_KEY=your_omdb_api_key_here


Run the application

python movies.py

🎬 Usage

Once the app starts, you’ll see a menu like:

Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Generate website


Example flow:

Choose 2. Add movie, enter a movie name (e.g., Inception).

The app fetches data from OMDb and saves it to movies.db.

Choose 9. Generate website → it builds index.html using your template and posters.

Open index.html in your browser to view your collection.


🧩 Website Preview

The generated site (index.html) uses the included template.html and style.css:

Displays movie posters in a centered grid

Shows each title and release year below the poster

Works immediately by opening the file locally in a browser

⚡ Error Handling

If the OMDb API is unreachable → prints a connection error.

If a movie is not found → prints “Movie not found”.

Invalid ratings or missing fields are replaced with safe defaults.


👨‍💻 Author

Patrick IOb
🎥 Movie Project — Python | SQLite | OMDb | HTML
📧 Contact: patrick.bauer.bit@gmail.com