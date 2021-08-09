from books.models import Genre
from django.core.exceptions import ObjectDoesNotExist


def get_selected_genre_from_request(request):
    genre_pk = None
    try:
        genre_pk = int(request.GET.get('genre'))
        if genre_pk == 0:
            genre_pk = None

    except TypeError:
        pass

    if genre_pk:
        try:
            return Genre.objects.get(pk=genre_pk)
        except ObjectDoesNotExist:
            return None
    else:
        return None