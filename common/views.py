from django.shortcuts import render
from django.urls import reverse
from common import models
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib import messages
def home(request):
    context = {
        "header" : models.Header.objects.last(),
        "teams" : models.Team.objects.all(),
        "fd" : models.FDS.objects.last(),
        "kp" : models.KPT.objects.last(),
        "socials" : models.Socials.objects.last(),
    }  
    return render(request, 'index.html', context)

def about(request):
    context = {
        "header" : models.Header.objects.last(),
        "intro" : models.Introduction.objects.last(),
        "images" : models.IntroImages.objects.all(),
        "fd" : models.FDS.objects.last(),
        "kp" : models.KPT.objects.last(),
        "socials" : models.Socials.objects.last(),
    }  

    return render(request, 'about.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
    
    try:
        models.Contacts.objects.create(name=name, email=email, subject=subject, message=message)
        messages.add_message(request, messages.SUCCESS, "Your message has been sent !!")
        return HttpResponseRedirect(reverse("common:home"))
    except Exception as e:
        print(e)
        messages.add_message(request, messages.WARNING, "There was a problem sending your message ! ")
        return HttpResponseRedirect(reverse("common:home"))
