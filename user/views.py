from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import SignUpForm,ProfileForm
from django.views.generic import CreateView,View,UpdateView
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from order.models import Order
# Create your views here.

class Login(LoginView):
    template_name = 'user_login.html'
    def form_valid(self, form):
        messages.success(self.request,'Logged in Successful')
        return super().form_valid(form)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name'] = self.request.user.username
    #     return context
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'user_signup.html'
    success_url = reverse_lazy('user_login')
    def form_valid(self, form):
        messages.success(self.request,'Signup Successfully')
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required,name='dispatch')
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('user_login')

@method_decorator(login_required,name='dispatch')
class Profile(UpdateView):
    model = User
    form_class=ProfileForm
    template_name= 'user_profile.html'
    success_url= reverse_lazy('home')
    def get_object(self, queryset=None):
        return self.request.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,'Profile Updated Successfully')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve orders for the current user
        orders = Order.objects.filter(user=self.request.user)
        context['orders'] = orders
        return context

@method_decorator(login_required,name='dispatch')
class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'PassChange.html'
    success_url = reverse_lazy('user_profile')
    def form_valid(self, form):
        messages.success(self.request,'Password Updated Successfully')
        return super().form_valid(form)