from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import LoginForm


class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, self.template_name, context={"form": LoginForm()})

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect('index')
