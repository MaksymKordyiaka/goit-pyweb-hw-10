from django.urls import path
from quotesapp.views.add_quote import AddQuoteView
from quotesapp.views.author_detail import AuthorDetailView
from quotesapp.views.index import IndexView, LogoutView
from quotesapp.views.login import LoginView
from quotesapp.views.register import RegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('add_quote/', AddQuoteView.as_view(), name='add_quote'),
    path('author/<int:author>/', AuthorDetailView.as_view(), name='author_detail'),
]