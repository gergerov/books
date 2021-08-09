from django.urls import path
from books.views.book.detail import BookDetailView
from books.views.author.detail import AuthorDetailView
from books.views.book.list import BookListView
from books.views.author.list import AuthorListView



urlpatterns = [
    path(
        'book/<int:pk>/read/'
        , BookDetailView.as_view()
        , name='book-detail'
        ),
    
    path(
        'book/list/'
        , BookListView.as_view()
        , name='book-list'
        ),
    
        path(
        'author/<int:pk>/read/'
        , AuthorDetailView.as_view()
        , name='author-detail'
        ),

        path(
        'author/list/'
        , AuthorListView.as_view()
        , name='author-list'
        ),
    
]