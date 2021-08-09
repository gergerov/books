from django.views.generic.list import ListView

from books.models import Book 


class BookListView(ListView):

    model = Book
    paginate_by = 120

    def dispatch(self, request, *args, **kwargs):
        self._set_request_parametrs(request)
        print(request.get_full_path())
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Book.books.search(search_string=self.search_string, genre_pk=self.genre_pk, author_pk=self.author_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список книг'
        return context

    def _set_request_parametrs(self, request):
        """Метод для вызова в dispatch. Анализирует get запрос, разруливая параметры"""
        genre_from_get = None
        try:
            genre_from_get = int(request.GET.get('genre'))
            if genre_from_get == 0:
                genre_from_get = None

        except TypeError:
            pass
        self.genre_pk = genre_from_get
        self.author_pk = request.GET.get('author')
        self.search_string = request.GET.get('search_string')
