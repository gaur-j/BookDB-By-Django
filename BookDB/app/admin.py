from django.contrib import admin
from.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price')  # Show these columns in admin panel
    search_fields = ('title', 'author')  # Add a search bar

admin.site.register(Book, BookAdmin)
