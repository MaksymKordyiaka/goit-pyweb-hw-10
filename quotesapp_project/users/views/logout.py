from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View


class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('index')
