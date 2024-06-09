from django.shortcuts import render, redirect
from django.views import View
from quotesapp.forms import QuoteForm


class AddQuoteView(View):
    template_name = 'quotesapp/add_quote.html'

    def get(self, request):
        form = QuoteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            quote.user = request.user
            quote.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})
