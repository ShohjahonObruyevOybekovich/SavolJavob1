from django.urls import path

from account.views import SignUpView, logout_view, account_view
from account.views import login_view

app_name = 'account'

urlpatterns = [
    path('sign',SignUpView.as_view(), name = 'sign'),
    path('logout/', logout_view, name='logout'),
    path('login',login_view, name = 'login'),
    path('account/',account_view, name = 'account_site')
]