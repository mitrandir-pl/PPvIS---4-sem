from dataclasses import dataclass


@dataclass
class Book:
    book_name: str = 'name'
    author_name: str = 'author_name'
    author_last_name: str = 'author_last_name'
    author_patronymic: str = 'author_patronymic'
    publisher: str = 'publisher'
    amount_of_volumes: int = 1
    circulation: int = 1000
    summary_volumes: int = amount_of_volumes*circulation
