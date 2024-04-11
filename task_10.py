# pip freeze > requirements.txt
# pip install Flask<2.0

from typing import List


class Audio:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

class Playlist:
    def __init__(self, name: str, genre: str):
        self.name = name
        self.genre = genre
        self.audios = []

    def add_audio(self, audio: Audio) -> None:
        self.audios.append(audio)

    def search_audio_by_name(self, name: str) -> List['Audio']:
        return [audio for audio in self.audios if audio.title == name]

    def search_playlist_by_name(self, name: str) -> List['Playlist']:
        # Search logic here
         return [self] if self.name == name else []

    def calculate_average_rating(self) -> float:
        # Rating calculation logic here
            pass

class User:
     def __init__(self, username: str):
        self.username = username
        self.ratings = []

     def add_rating(self, rating: int) -> None:
        self.ratings.append(rating)

     def calculate_average_rating(self) -> float:
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)

# Example usage:
audio1 = Audio("Song 1", "https://example.com/song1.mp3")
playlist1 = Playlist("My Playlist", "Pop")
playlist1.add_audio('audio1')
user1 = User("John")
user1.add_rating(4)
user1.add_rating(5)
average_rating = user1.calculate_average_rating()
print(f"Average rating for {user1.username}: {average_rating:.2f}")

