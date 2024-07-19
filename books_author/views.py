from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book

class HomePageView(TemplateView):
    template_name = 'home.html'

class BookListView(ListView):
    template_name = 'list_of_books.html'
    model = Book
    context_object_name = 'books' # Default Name: object_list

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['books'] = Book.objects.all()
    #     return context

class BookDetailsView(DetailView):
    model = Book
    template_name = 'book_details.html'  # Default Name: pet >>> (table name)