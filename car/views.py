from django.views.generic import DetailView,CreateView
from django.urls import reverse_lazy
from .models import Car
from comment.models import Comment
from comment.forms import Review

class CarDetail(DetailView,CreateView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'
    slug_url_kwarg = 'car_slug'
    form_class = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        context['related_cars'] = Car.objects.filter(price__gte=car.price)
        context['comments'] = Comment.objects.filter(car=car)
        return context

    def form_valid(self, form):
        form.instance.car = self.get_object()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('car_details', kwargs={'car_slug': self.kwargs['car_slug']})
    