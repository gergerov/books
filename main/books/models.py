from django.conf import settings
from django.db import models

from base_models.abstract.with_absolute_url_model import WithAbsoluteUrlModel
from base_models.abstract.avatar import Avatar
from base_models.abstract.people import People

from ckeditor_uploader.fields import RichTextUploadingField

from books.managers import BookManager, AuthorManager


class Genre(models.Model):
    """Модель жанра"""
    title = models.CharField(verbose_name="Название", max_length=64, default="Жанр", unique=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Author(People, Avatar, WithAbsoluteUrlModel):
    """Модель автора книги"""

    biography = models.TextField(verbose_name="Биография", null=False, default="Биография", max_length=4096)

    objects = models.Manager()
    authors = AuthorManager()
    
    absolute_url_name = 'author-detail'
    default_avatar_path = settings.MEDIA_URL + 'no_foto.jpg'

    def __str__(self) -> str:
        return super().__str__()

    @property
    def avatar_upload_path(self) -> str:
        """Переопределенный метод класса Avatar: формирование папки для сохранения аватарки"""
        return f'authors/{self.surname} {self.name} {self.patronymic} {str(self.date_born)}'

    class Meta:
        db_table = 'authors'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    # def save(self, *args, **kwargs) -> None:
    #     return super().save(*args, **kwargs)

    def get_author_avatar(self):
        return self.get_avatar_url(300)


class Book(WithAbsoluteUrlModel, Avatar):
    """Модель книги"""
    
    title = models.CharField(verbose_name="Название книги", max_length=64, default="Приключения Тома Сойера", unique=False)
    description_short = RichTextUploadingField(verbose_name="Краткое описание", max_length=2048, default="Краткое описание")
    description_long = RichTextUploadingField(verbose_name="Описание книги", max_length=1000000, default="Подробное описание")
    date = models.DateField(verbose_name="Дата написания книги")
    authors = models.ManyToManyField(to=Author, verbose_name="Авторы")
    genres = models.ManyToManyField(to=Genre, verbose_name="Жанры")
    

    books = BookManager()
    objects = models.Manager()
    absolute_url_name = 'book-detail'
    default_avatar_path = settings.MEDIA_URL + 'no_foto.jpg'

    class Meta:
        ordering = ['title', '-date']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self) -> str:
        authors = self.authors.filter()
        authors_str = ''
        for a in authors:
            authors_str += str(a) + ' '

        return f'"{self.title}" , авторы: {authors_str} , год написания: {self.date} .'

    @property
    def get_authors_string(self):
        authors = self.authors.all()
        authors_string = ''
        for a in authors:
            authors_string += a.surname + ' ' + a.name + ' ' + a.patronymic + '; '
        return authors_string

    @property
    def get_genres_string(self):
        genres = self.genres.all()
        genres_string = ''
        for g in genres:
            genres_string += g.title + '; '
        return genres_string

    @property
    def avatar_upload_path(self) -> str:
        """Переопределенный метод класса Avatar: формирование папки для сохранения аватарки"""
        return f'books/{self.title} {str(self.date)} {self.pk}'

    def get_book_avatar(self):
        return self.get_avatar_url(300)

