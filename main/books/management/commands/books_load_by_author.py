from django.core.management.base import BaseCommand, CommandError
from books.services.google_books.load_books_from_google import BookLoaderByAuthorFromGoogle

class Command(BaseCommand):
    help = '\tЗагружает книги с google.books.api по введенному автору в БД'

    def handle(self, *args, **options):
        loader = BookLoaderByAuthorFromGoogle(author_id=options['author_id'])
        loader.insert_books

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=int)


