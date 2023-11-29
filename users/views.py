from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView 
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import *
from django.urls import reverse, reverse_lazy


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизація'}
    def get_success_url(self):
        return reverse_lazy('index')

""" def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
               
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginUserForm()
    context = {'form': form}
    return render(request, 'login.html', context)
 """

def register(request):
    return render(request, 'register.html')

def user_logout(request):
    return render(request, 'logout.html')

def user_profile(request):
    return render(request, 'profile.html')

def user_edit_profile(request):
    return render(request, 'edit_profile.html')

def user_change_password(request):
    return render(request, 'change_password.html')


