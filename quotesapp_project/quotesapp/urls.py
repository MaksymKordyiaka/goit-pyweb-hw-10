from django.urls import path
from quotesapp.views.add_quote import AddQuoteView
from quotesapp.views.author_detail import AuthorDetailView
from quotesapp.views.index import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_quote/', AddQuoteView.as_view(), name='add_quote'),
    path('author/<int:author>/', AuthorDetailView.as_view(), name='author_detail'),
]
