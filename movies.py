import random
import movie_storage_sql as movie_storage
import data_fetcher


def greeting():
    """Greets the user"""
    print(">.>.>.>.>.>oO My Movies Database Oo<.<.<.<.<.<")


def menu():
    """Displays the menu to the user"""
    print("""Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Generate Website""")
    print()


def print_all_movies(movies=None):
    """Prints all movies"""
    if movies is None:
        movies = movie_storage.get_movies()

    print(f"{len(movies)} movies in total\n")
    for title, info in movies.items():
        print(f"{title} ({info['release_year']}): {info['rating']}")


def add_movie():
    """Adds a new movie using IMDb (only ask for title)"""
    movies = movie_storage.get_movies()

    while True:
        movie_name = input("Give me the movie's name: ").strip()
        if movie_name:
            break
        print("Movie name cannot be empty!")

    if movie_name in movies:
        print("Movie already exists!")
        return

    # Fetch from OMDb
    try:
        data = data_fetcher.fetch_data(movie_name)
    except Exception:
        print("Could not reach OMDb API. Check your internet connection.")
        return

    # Movie not found
    if not data or str(data.get("Response")).lower() == "false":
        print(f"Movie '{movie_name}' was not found in IMDb.")
        return

    # Extract fields directly from IMDb data
    title = data.get("Title") or movie_name
    year = data.get("Year")
    rating = data.get("imdbRating")
    poster_url = data.get("Poster")

    # Handle missing or "N/A" fields
    if year in (None, "", "N/A"):
        year = 0  # or you could just skip adding the movie instead
    if rating in (None, "", "N/A"):
        rating = 0.0
    else:
        rating = float(rating)
    if poster_url in (None, "", "N/A"):
        poster_url = None

    # Save to DB
    movie_storage.add_movie(title, int(year), rating, poster_url)

    print("\nUpdated Movie List:")
    print_all_movies()

def del_movie():
    """Delete a movie by name entered by user"""
    movies = movie_storage.get_movies()

    while True:
        movie_to_delete = input("Give me the name of the movie you want to delete: ").strip()
        if movie_to_delete:
            break
        print("Movie name cannot be empty!")

    if movie_to_delete in movies:
        movie_storage.delete_movie(movie_to_delete)
        print("Movie deleted.")
    else:
        print("Movie not found.")

    print_all_movies()


def update_movie():
    """Update an existing movie rating"""
    movies = movie_storage.get_movies()

    while True:
        movie_to_update = input("Which movie do you want to update? ").strip()
        if movie_to_update:
            break
        print("Movie name cannot be empty!")

    if movie_to_update in movies:
        while True:
            try:
                new_rating = float(input("What is the updated rating? "))
                if 1 <= new_rating <= 10:
                    break
                else:
                    print("Rating must be between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

        movie_storage.update_movie(movie_to_update, new_rating)
        print("Movie updated.")
    else:
        print("Movie not found.")

def stats_movies():
    """Print stats like average, best and worst"""
    movies = movie_storage.get_movies()

    ratings = [info["rating"] for info in movies.values()]
    average = sum(ratings) / len(ratings)
    best = max(movies, key=lambda t: movies[t]["rating"])
    worst = min(movies, key=lambda t: movies[t]["rating"])

    print(f"\nAverage Rating is {round(average, 1)}")
    print(f"Best Movie is {best} ({movies[best]['rating']})")
    print(f"Worst Movie is {worst} ({movies[worst]['rating']})")


def random_movie():
    """Print a random movie"""
    movies = movie_storage.get_movies()

    title = random.choice(list(movies.keys()))
    info = movies[title]
    print(f"{title} ({info['release_year']}): {info['rating']}")


def search_movie():
    """Search for a specific movie"""
    movies = movie_storage.get_movies()

    while True:
        searching = input("What movie are you searching for? ").strip()
        if searching:
            break
        print("Search term cannot be empty!")

    found = False
    for title, info in movies.items():
        if searching.lower() in title.lower():
            print(f"{title} ({info['release_year']}): {info['rating']}")
            found = True
    if not found:
        print("No Movie was found")


def sort_movies():
    """Sort movies by rating descending"""
    movies = movie_storage.get_movies()

    sorted_movies = dict(sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True))
    print_all_movies(sorted_movies)

def generate_website():
    """Generate a website for all movies added"""
    movies = movie_storage.get_movies()

    # Build <li> items that match style.css classes
    items = []
    for title, info in movies.items():
        poster = info.get("poster_url") or ""
        year = info.get("release_year", "")
        items.append(
            f"""
            <li>
              <div class="movie">
                <img class="movie-poster" src="{poster}" alt="Poster for {title}">
                <p class="movie-title">{title}</p>
                <p class="movie-year">{year}</p>
              </div>
            </li>
            """.strip()
        )

    grid_html = "\n".join(items)

    # Load template.html (the one with __TEMPLATE_MOVIE_GRID__)
    with open("index_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Inject the grid and write index.html
    html = template.replace("__TEMPLATE_MOVIE_GRID__", grid_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Website was generated successfully.")



def main():
    """Main function"""
    greeting()

    while True:
        print("\n")
        menu()
        try:
            users_choice = int(input("Enter choice (0-9): "))
        except ValueError:
            print("Please enter a number between 0 and 9.")
            continue

        print()

        if users_choice == 0:  # Exit the Program
            print("Bye!")
            break
        elif users_choice == 1:  # List
            print_all_movies()
        elif users_choice == 2:  # Add
            add_movie()
        elif users_choice == 3:  # Delete
            del_movie()
        elif users_choice == 4:  # Update
            update_movie()
        elif users_choice == 5:  # Stats
            stats_movies()
        elif users_choice == 6:  # Random
            random_movie()
        elif users_choice == 7:  # Search
            search_movie()
        elif users_choice == 8:  # Sort
            sort_movies()
        elif users_choice == 9: # generate website
            generate_website()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()