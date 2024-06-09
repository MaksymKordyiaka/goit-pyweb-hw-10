from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View
from quotesapp.models import Quote


class IndexView(View):
    template_name = 'quotesapp/index.html'

    def get(self, request):
        quotes = Quote.objects.all()
        paginator = Paginator(quotes, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')