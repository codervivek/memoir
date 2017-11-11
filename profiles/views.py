from django.shortcuts import render

# Create your views here.
from memoir.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.models import Max
from django.views import generic
from django.contrib.auth.models import User
from memoir.forms import SignUpForm
from .models import Department
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    department=Department.objects.all()
    return render(request,'index.html', {'department_list':department})

from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View

from iitgauth.views import WebmailLoginView


class LoginView(WebmailLoginView):
    """
    View class which handles logging in users. It is subclass of
    ``WebmailLoginView`` class provided by ``iitgauth`` package.
    """
    template_name = 'profiles/login.html'
    success_url = reverse_lazy('home')


class HomeView(LoginRequiredMixin, TemplateView):
    """
    View class for rendering home page with user added to context.
    """
    login_url = reverse_lazy('login')
    template_name = 'profiles/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class LogoutView(LoginRequiredMixin, View):
    """
    View class which handles logging out users.
    """
    login_url = reverse_lazy('login')
    http_method_names = ['get', 'head', 'options']

    def get(self, request):
        auth.logout(request)
        return redirect('login')