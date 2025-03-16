from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

def home(request):
    return render(request, 'home.html')

def add_book(request):
    if request.method == "POST":
        if form.is_vaild():
            form.save()
            return redirect('book_list')
    else :
        form = BookForm()
    return render (request, 'add_book.html', {'form': form})

@login_required
def dashboard(request):
    return render (request, 'dashboard.html')

@api_view(['GET', 'POST'])  # Add 'POST'
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':  # Allow adding books via API
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)