from django.shortcuts import render, redirect
from .models import Feedback

# Create your views here.

def home(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message= request.POST.get("message")
        
        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect("/")

    return render(request, "feedback/index.html")