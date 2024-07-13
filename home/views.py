from django.shortcuts import render
from .models import Messages


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        if name and email and message:
            messageData = Messages(name=name, email=email, message=message)
            messageData.save()

    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')
