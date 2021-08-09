from django.db import models


class BookManager(models.Manager):
    def search(self, search_string=None, genre_pk=None, author_pk=None):
        genre_filter = models.Q(genres__pk=genre_pk)
        author_filter = models.Q(authors__pk=author_pk)
        search_string_filter = (
                models.Q(title__icontains=search_string)|
                models.Q(description_short__icontains=search_string)|
                models.Q(description_long__icontains=search_string)|
                models.Q(genres__title__icontains=search_string)|
                models.Q(authors__name__icontains=search_string)|
                models.Q(authors__surname__icontains=search_string)
            )
        q = self.get_queryset().all()
        if search_string:
            q = q.filter(search_string_filter)
        if genre_pk:
            q = q.filter(genre_filter)
        if author_pk:
            q = q.filter(author_filter)
        
        return q.distinct()

    def create_from_google(self, title, description, date, author, genre):
        created = True
        if not self.get_queryset().filter(authors__pk=author.pk, title=title).exists():
            object = self.get_queryset().create(
                description_long = description,
                description_short = description,
                title = title,
                date = date,
            )
            object.save()
            object.authors.add(author)
            object.genres.add(genre)
        else:
            created = False
            object = None
        return object, created


class AuthorManager(models.Manager):
    def search(self, search_string=None):
        search_string_filter = (
            models.Q(name__icontains=search_string)|
            models.Q(surname__icontains=search_string)|
            models.Q(patronymic__icontains=search_string)
        )
        q = self.get_queryset().all()
        if search_string:
            q = q.filter(search_string_filter)
        return q
