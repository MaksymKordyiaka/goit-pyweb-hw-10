from django.shortcuts import render, get_object_or_404
from django.views import View
from quotesapp.models import Author


class AuthorDetailView(View):
    template_name = 'quotesapp/author_detail.html'

    def get(self, request, author):
        author_instance = get_object_or_404(Author, pk=author)
        return render(request, self.template_name, {'author': author_instance})
