from books.services.google_books.search_books_by_author import search_books_by_author
from django.core.exceptions import ObjectDoesNotExist
from books.models import Author, Book, Genre


class BookLoaderByAuthorFromGoogle:
    def __init__(self, author_id) -> None:
        self.set_author(author_id=author_id)

    def set_author(self, author_id):
        try:
            self.author = Author.objects.get(pk=author_id)
        except ObjectDoesNotExist:
            raise f"Автора с id {author_id} не существует"

    def set_books(self):
        author_fio = self.author.surname + ' ' + self.author.name + ' ' +  self.author.patronymic
        self.books = search_books_by_author(author_fio)

    def set_genres(self):
        self.genre = Genre.objects.get(pk=5)

    def insert_books(self):
        for book in self.books:
            object, created = Book.books.create_from_google(book['title'], book['description'], '2000-01-01', self.author, self.genre)
            if created:
                print(f"Книга {object} сохранена.")
            else:
                print(f"Книга {book['title']} автора {self.author} уже записана")
                