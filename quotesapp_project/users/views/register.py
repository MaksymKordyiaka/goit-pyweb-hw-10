from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from users.forms import RegisterForm


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, self.template_name, context={"form": RegisterForm()})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, self.template_name, context={"form": form})
