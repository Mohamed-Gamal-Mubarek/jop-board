import django_filters
from .models import Job
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = '__all__'