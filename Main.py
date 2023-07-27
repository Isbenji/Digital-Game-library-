class Game:
    def __init__(self, title, genre, platform):
        self.title = title
        self.genre = genre
        self.platform = platform

class GameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game):
        self.games.remove(game)

    def search_game(self, title):
        for game in self.games:
            if game.title.lower() == title.lower():
                return game
        return None

    def display_library(self):
        if not self.games:
            print("The library is empty.")
        else:
            print("Game Library:")
            for game in self.games:
                print(f"Title: {game.title}, Genre: {game.genre}, Platform: {game.platform}")


# Create a game library
library = GameLibrary()

# Add games to the library
game1 = Game("The Legend of Zelda: Breath of the Wild", "Action-Adventure", "Nintendo Switch")
game2 = Game("Red Dead Redemption 2", "Action-Adventure", "PlayStation 4")
game3 = Game("Minecraft", "Sandbox", "PC")

library.add_game(game1)
library.add_game(game2)
library.add_game(game3)

# Display the library
library.display_library()

# Search for a game
search_title = input("Enter a game title to search: ")
search_result = library.search_game(search_title)

if search_result:
    print("Game found:")
    print(f"Title: {search_result.title}, Genre: {search_result.genre}, Platform: {search_result.platform}")
else:
    print("Game not found.")

# Remove a game
remove_title = input("Enter a game title to remove: ")
remove_result = library.search_game(remove_title)

if remove_result:
    library.remove_game(remove_result)
    print(f"{remove_result.title} has been removed from the library.")
else:
    print("Game not found.")

# Display the updated library
library.display_library()
