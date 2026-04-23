from __future__ import annotations
from dataclasses import dataclass, field, asdict
import json


@dataclass(frozen=True)
class Movie:
    rating: int | float = field(compare=True)
    title: str = field(compare=False)

    def __post_init__(self):
        if not isinstance(self.rating, (int, float)):
            raise ValueError("Rating must be an integer or float")
        if not isinstance(self.title, str):
            raise ValueError("Title must be a string")
        if self.title.strip() == "":
            raise ValueError("Title cannot be empty")
        if not (1 <= self.rating <= 10):
            raise ValueError("Rating must be between 1 and 10")

    def display_info(self) -> str:
        return f"{self.title} has a rating of {self.rating}"

    @property
    def is_recommended(self) -> bool:
        return self.rating >= 8

    def to_dict(self) -> dict[str, any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict[str, any]) -> Movie:
        return Movie(**data)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> Movie:
        return Movie.from_dict(json.loads(json_str))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Movie):
            return NotImplemented
        return self.rating == other.rating and self.title == other.title

    def __hash__(self) -> int:
        return hash((self.rating, self.title))

    def __lt__(self, other: Movie) -> bool:
        if not isinstance(other, Movie):
            return NotImplemented
        return self.rating < other.rating


def main():
    movie = Movie(8.9, "The Matrix")
    print(movie.display_info())
    print(f"Is recommended: {movie.is_recommended}")
    print(movie.to_dict())
    print(movie.to_json())

    movie2 = Movie.from_dict({"rating": 7.5, "title": "Inception"})
    print(movie2.display_info())

    movie3 = Movie.from_json(movie.to_json())
    print(movie3.display_info())
    print(movie == movie3)  # True
    print(movie < movie2)   # False


if __name__ == "__main__":
    main()