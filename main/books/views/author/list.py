from django.views.generic.list import ListView

from books.models import Author 

class AuthorListView(ListView):

    model = Author
    paginate_by = 60

    def dispatch(self, request, *args, **kwargs):
        self.set_request_parametrs(request)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Author.authors.search(search_string=self.search_string)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список авторов'
        return context

    def set_request_parametrs(self, request):
        """Метод для вызова в dispatch. Анализирует get запрос, разруливая параметры"""
        self.search_string = request.GET.get('author_search_string')
