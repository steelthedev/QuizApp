
from django.urls import path
from django.urls.conf import include
from . import views

app_name="app"

urlpatterns = [
    path('', views.Home, name="home"),
    path('quiz',views.Quiz , name="quiz")
]
