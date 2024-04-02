from django.urls import path
from . import views
urlpatterns = [
    path('<slug:car_slug>/',views.CarDetail.as_view(),name='car_details')
]
