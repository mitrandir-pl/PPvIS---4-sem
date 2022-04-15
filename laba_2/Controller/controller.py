import xml.sax

from Utility.xml_parsers import Reader, Writer
from Model.model import Book


class DataBaseController:

    def __init__(self):
        self._reader = Reader()
        self._writer = Writer('Utility/test.xml')
        self._list_of_books = list()
        self.read_from_file()

    def add_book(self, book):
        self._list_of_books.append(book)
        print(self._list_of_books)

    def get_all_books(self):
        return self._list_of_books

    def search_by_author_last_name(self, author_last_name):
        found_books = list()
        for book in self._list_of_books:
            if book.author_last_name == author_last_name:
                found_books.append(book)
        return found_books

    def search_by_author_last_name_and_publisher(self, author, publisher):
        found_books = list()
        for book in self._list_of_books:
            if book.author_last_name == author and book.publisher == publisher:
                found_books.append(book)
        return found_books

    def search_by_amount_of_volumes(self, amount_of_volumes):
        found_books = list()
        for book in self._list_of_books:
            if int(book.amount_of_volumes) == int(amount_of_volumes):
                found_books.append(book)
        return found_books

    def delete_by_author_last_name(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_books)):
            if self._list_of_books[index].author_last_name == input_:
                self._list_of_books.remove(self._list_of_books[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_author_and_publisher(self, input_):
        author, publisher = input_.split()
        counter = 0
        index = 0
        for _ in range(len(self._list_of_books)):
            if self._list_of_books[index].author_last_name == author \
                    and self._list_of_books[index].author_last_name == publisher:
                self._list_of_books.remove(self._list_of_books[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_amount_of_volumes(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_books)):
            if int(self._list_of_books[index].amount_of_volumes) == int(input_):
                self._list_of_books.remove(self._list_of_books[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_book_name(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_books)):
            if self._list_of_books[index].book_name == input_:
                self._list_of_books.remove(self._list_of_books[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_less_than_amount_of_volumes(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_books)):
            if int(self._list_of_books[index].amount_of_volumes) < int(input_):
                self._list_of_books.remove(self._list_of_books[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_more_than_amount_of_volumes(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_books)):
            if int(self._list_of_books[index].amount_of_volumes) > int(input_):
                self._list_of_books.remove(self._list_of_books[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def write_data_into_file(self):
        print(self._list_of_books)
        for book in self._list_of_books:
            self._writer.create_xml_client({
                "book_name": book.book_name,
                "author_name": book.author_name,
                "author_last_name": book.author_last_name,
                "author_patronymic": book.author_patronymic,
                "publisher": book.publisher,
                "amount_of_volumes": book.amount_of_volumes,
                "circulation": book.circulation,
            })
        self._writer.create_xml_file()

    def read_from_file(self):
        parser = xml.sax.make_parser()
        parser.setContentHandler(self._reader)
        parser.parse('Utility/test.xml')
        for book in self._reader.data_table:
            self._list_of_books.append(Book(
                book[0], book[1], book[2], book[3],
                book[4], book[5], book[6],
            ))
        print(self._list_of_books)
        print(self._list_of_books)
