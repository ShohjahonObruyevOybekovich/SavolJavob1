
from random import sample

from django.contrib.auth import authenticate, login
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from account.forms import SignUpForm, LoginForm
from account.models import CustomUser
from app.filters import ResultFilter
from app.models import Category, Question, Result
from app.services import check_answer


class HomePage(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()

        return render(request, 'home.html', {'categories': categories})


class CategoriesView(View):

    def get(self, request, id, *args, **kwargs):
        category = Category.objects.get(id=id)
        questions = Question.objects.filter(category=category)


        return render(request, 'app/categories.html', {'questions': questions})

    def post(self, request, id, *args, **kwargs):
        category = Category.objects.get(id=id)
        questions = Question.objects.filter(category=category)
        questions = sample(list(questions), 3)
        if cache.get('questions'):
            questions = cache.get('questions')
        else:
            cache.set('questions',questions)
        if request.method == 'POST':

            context = check_answer(request, questions, category)
            return render(request, 'app/result.html', context)

def result_list(request):
    filter = ResultFilter(request.GET, queryset=Result.objects.all())

    context = {'filter': filter}
    return render(request,'app/result_list.html',context)