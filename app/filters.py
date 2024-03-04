import django_filters
from django import forms
from .models import Result

class ResultFilter(django_filters.FilterSet):

    data_gt = django_filters.NumberFilter(field_name='create_at', lookup_expr='gt', widget=forms.DateInput(attrs={'type': 'date'}))
    data_lt = django_filters.NumberFilter(field_name='create_at', lookup_expr='lt',widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Result
        fields = ['user__phone', 'data_gt',
                  'data_lt']