from django.urls import path
from.views import book_list, add_book

urlpatterns = [
    path('api/books/', book_list, name='book-list'),
    path('api/books/add/', add_book, name='add-book'),
]

def load_views():
    from .views import home  # Import inside function to avoid circular imports
    global urlpatterns
    urlpatterns.append(path('', home, name='home'))

load_views()
