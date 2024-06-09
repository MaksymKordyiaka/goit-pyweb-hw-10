from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


class LoginView(View):
    template_name = 'quotesapp/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, self.template_name, {'form': form})
