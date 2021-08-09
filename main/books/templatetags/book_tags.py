from django import template
from books.models import Genre
from books.utils import get_selected_genre_from_request
register = template.Library()



@register.inclusion_tag('books/elements/book_search.html')
def book_search_panel(request, placeholder="Война и мир"):
    genres = Genre.objects.all()
    selected_genre = get_selected_genre_from_request(request)
    search_string = request.GET.get('search_string')
    if search_string is None:
        search_string = ''
        
    return {
        "selected_genre": selected_genre,
        "search_string": search_string,
        "placeholder": placeholder,
        "genres": genres 
    }


@register.inclusion_tag('books/elements/author_search.html')
def author_search_panel(request, placeholder="Достоевский Федор Михайлович"):
    author_search_string = request.GET.get('author_search_string')
    if author_search_string is None:
        author_search_string = ''
        
    return {
        "author_search_string": author_search_string,
        "placeholder": placeholder,
    }
