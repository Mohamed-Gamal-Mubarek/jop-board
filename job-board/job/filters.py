import django_filters
from .models import Job

# https://github.com/carltongibson/django-filter/tree/78210722d920f803a8142e48969bc37f0f8324ed

# DOCUMENTATION
# https://django-filter.readthedocs.io/en/stable/guide/usage.html

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['published_at', 'img', 'salary', 'vacancy', 'slug', 'owner', 'description']