from audioop import reverse

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import CreateView

from account.forms import SignUpForm, LoginForm

User = get_user_model()
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'account/sign.html'
    success_url = '/'

def logout_view(request):
    logout(request)
    return redirect(('account:login'))
def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:home')

    return render(request, 'account/login.html', {'form': form})

def account_view(request):
    user = User.objects.get(pk=request.user.pk)
    context = {
        'user': user,
    }
    return render(request, 'account/account_site.html', context)
