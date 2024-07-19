from django.contrib import admin
from django.urls import path
from .views import HomePageView, BookListView, BookDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailsView.as_view(), name='details'),
]
