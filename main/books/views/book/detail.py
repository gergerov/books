from django.views.generic.detail import DetailView
from books.models import Book


class BookDetailView(DetailView):

    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.get_object().title}'
        return context