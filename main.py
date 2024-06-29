class Movie:
    def __init__(self, title, director, year, genre, studio):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.studio = studio

    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director}, Genre: {self.genre}, Studio: {self.studio}"
    
class MovieCatalog:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def list_movies(self):
        for movie in self.movies:
            print(movie)

    def search_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                print(movie)
                return
        print("Movie not found")

    def remove_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                self.movies.remove(movie)
                print("Movie has been removed!")
            else:
                print("We can't find that movie. Try again.")

def display_menu():
    print("Welcome to MovieJab!")
    print("1. Add a movie")
    print("2. List all movies")
    print("3. Search all movies")
    print("4. Remove a movie")
    print("5. Exit")

def main():
    catalog = MovieCatalog()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter movie title: ")
            director = input("Enter director: ")
            year = int(input("Enter year of movie's release: "))
            genre = input("Enter a genre: ")
            studio = input("Enter the film's studio: ")
            movie = Movie(title, director, year, genre, studio)
            catalog.add_movie(movie)
            print("Movie has been added to your collection!")
        elif choice == '2':
            catalog.list_movies()
        elif choice == '3':
            title = input("Enter a title to search: ")
            catalog.search_movie(title)
        elif choice == '4':
            title = input("Enter the title you would like to remove: ")
            catalog.remove_movie(title)
            print("Movie has been removed!")
        elif choice == '5':
            print("Shutting down the app...")
            break
        else:
            print("Invalid. Please try again.")

if __name__ == "__main__":
    main()