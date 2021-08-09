from django.contrib.admin.decorators import register
from django.contrib import admin
from django.contrib import messages

from books.services.google_books.load_books_from_google import BookLoaderByAuthorFromGoogle
from books.models import Author, Genre, Book


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'patronymic', 'date_born', 'sex', 'image',)
    search_fields = ('name', 'surname', 'patronymic',)
    list_filter = ('sex',)
    actions = ['load_books_from_google_by_author']

    def load_books_from_google_by_author(self, request, queryset):
        """Загрузить книги с google books по автору"""
        authors = queryset.values_list('pk', flat=True)
        for author in authors:
            loader = BookLoaderByAuthorFromGoogle(author)
            loader.set_genres()
            loader.set_books()
            loader.insert_books() 
        
        self.message_user( request, 'Книги загружены.', messages.SUCCESS )


@register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    search_fields = ('title',)


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'date', )
    search_fields = ('title',)
    list_filter = ('genres', 'authors',)
