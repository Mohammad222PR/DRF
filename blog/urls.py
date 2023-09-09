from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('blog', views.home, name='home'),
    path('blog/home', views.Home.as_view(), name='home'),

]
