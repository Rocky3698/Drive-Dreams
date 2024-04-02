from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from car.models import Car
from brand.models import Brand

def home(request):
    return render(request,'base.html')


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        brand_slug = self.kwargs.get('brand_slug')
        if brand_slug is not None and brand_slug != 'all-brand':
            brand = Brand.objects.get(slug=brand_slug)
            return Car.objects.filter(brand=brand)
        else:
            return Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context