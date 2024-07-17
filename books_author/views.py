from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book

class HomePageView(TemplateView):
    template_name = 'home.html'

class BookListView(TemplateView):
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context
