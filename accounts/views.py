from django.shortcuts import render
from django.contrib.auth.hashers import BasePasswordHasher, make_password, check_password
from .models import Token
import random
# Create your views here.

def GenerateToken(request):
    if request.user.is_authenticated:
        random_word= "t-o-k-e-n"
        random_int = random.randint(0,100)
        random_ = f"{random_word} + {random_int}"
        token = make_password(random_)
        Token.objects.create(token=token)
    return render(request, "accounts/token.html")

