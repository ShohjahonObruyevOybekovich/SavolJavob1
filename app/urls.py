from django.urls import path

from app.views import HomePage, CategoriesView, result_list

app_name = 'app'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('english/<int:id>', CategoriesView.as_view(), name='categories'),
    path('Results', result_list, name='results_list'),

]


