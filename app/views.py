import datetime
from django.shortcuts import redirect, render
from .models import QuestionModel
from accounts.models import Token
from datetime import date, time, timedelta, datetime
from django.contrib.auth.hashers import check_password
from django.contrib import messages
import pytz
# Create your views here.


def Home(request):
    if request.method == "POST":
        name= request.POST["name"]
        email= request.POST["email"]
        token = request.POST["token"]

        if name and token and email:
            try:
                token_check = Token.objects.get(token=token)
            except:
                messages.info(request, "Invalid or Expired Token")
                return redirect("app:home")

            if token_check:
                utc=pytz.UTC
                token_date = token_check.date_created
                time_estimate = timedelta(hours=2) + token_date
                now = datetime.now()
                now_= utc.localize(now)
                if now_ >= time_estimate:
                    return redirect("app:home")
                else:
                    return redirect("app:quiz")
            else:
                None
    return render(request, 'app/index.html')



def Quiz(request):
    if request.method == "POST":
        
        questions=QuestionModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total +=1
            if q.ans ==  request.POST.get(q.question):
                score += 1
                correct += 1
            else:
                wrong+=1
        percent = score/(total*40) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request, 'app/quiz.html', context)   
    return render(request, 'app/quiz.html')            