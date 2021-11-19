from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('token_generate', views.GenerateToken, name="generate_token"),
]
