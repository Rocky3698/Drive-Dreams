from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Car, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


login_required
def Order(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    user = request.user

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.instance.user = user
            order_form.instance.car = car
            quantity = order_form.cleaned_data['quantity']
            order_form.instance.total_price = car.price * quantity
            order_form.save()
            car.quantity -= quantity
            car.save()
            messages.success(request, "Your order is confirmed. Thank you for shopping with us.")
            return redirect('home')
    else:
        # Pre-populate the form with the default quantity (e.g., 1)
        order_form = OrderForm(initial={'quantity': 1})
    return render(request, 'order.html', {'form': order_form, 'user': user, 'car': car})
