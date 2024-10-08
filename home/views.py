from django.shortcuts import render
from .models import Messages
from .utils import generate_response


def index(request):
    if request.method == "POST":
        if "contact-form" in request.POST:    
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            
            if name and email and message:
                messageData = Messages(name=name, email=email, message=message)
                messageData.save()
        
        if "question-form" in request.POST:
            prompt = request.POST.get("question")
            if prompt.strip() == '':
                return render(request, 'index.html')
            response = generate_response(prompt)
            return render(request, 'index.html', {'answer': response})



    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')
