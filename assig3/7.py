from __future__ import annotations
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Song:
    duration: float = field(compare=True)
    title: str = field(compare=False)

    def __post_init__(self):
        if not isinstance(self.title, str) or self.title.strip() == "":
            raise ValueError("Title must be a non-empty string")
        if not isinstance(self.duration, (int, float)) or self.duration <= 0:
            raise ValueError("Duration must be a positive number")

    def __str__(self) -> str:
        return f"{self.title} ({self.duration} min)"


@dataclass
class Playlist:
    name: str
    songs: list[Song] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.name, str) or self.name.strip() == "":
            raise ValueError("Playlist name must be a non-empty string")

    def add_song(self, song: Song) -> None:
        if not isinstance(song, Song):
            raise ValueError("Only Song instances can be added")
        self.songs.append(song)

    def total_duration(self) -> float:
        return sum(song.duration for song in self.songs)

    def longest_song(self) -> Song | None:
        if not self.songs:
            return None
        return max(self.songs, key=lambda s: s.duration)

    def show_playlist(self) -> None:
        if not self.songs:
            print(f"Playlist '{self.name}' is empty")
            return
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"  - {song}")
        print(f"Total duration: {self.total_duration()} min")
        print(f"Longest song: {self.longest_song()}")


def main():
    playlist = Playlist(name="My Favorites")

    playlist.add_song(Song(title="Bohemian Rhapsody", duration=5.55))
    playlist.add_song(Song(title="Stairway to Heaven", duration=8.02))
    playlist.add_song(Song(title="Hotel California", duration=6.30))
    playlist.add_song(Song(title="Blinding Lights", duration=3.20))

    playlist.show_playlist()


if __name__ == "__main__":
    main()