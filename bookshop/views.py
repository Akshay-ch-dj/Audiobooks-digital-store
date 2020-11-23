from django.shortcuts import render
from bookshop.models.book import Book

# Create your views here.


def index(request):
    """View for the index page
    """
    books = Book.objects.all()
    print(books)
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
