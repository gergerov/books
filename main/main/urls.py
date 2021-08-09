from django.contrib import admin

from django.conf.urls import include, static
from django.conf import settings

from django.urls import path
from django.views.generic.base import RedirectView



urlpatterns = [
     path('admin/', admin.site.urls)
    , path("ckeditor/", include('ckeditor_uploader.urls'))
    , path("books/", include('books.urls'))
    , path("", RedirectView.as_view(pattern_name='book-list', permanent=True), name='index')
]
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
