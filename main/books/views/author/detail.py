from books.models import Author
from django.views.generic.detail import DetailView


class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.get_object()}'
        return context