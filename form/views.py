from django.shortcuts import render
from .forms import ContactForm
from .models import Contactdata
from django.contrib import messages

def insertdata(request):
    if request.method == "POST":
        if request.POST.get('naam') and request.POST.get('email') and request.POST.get('onderwerp') and request.POST.get('bericht'):
            saverecord = Contactdata()
            saverecord.naam = request.POST.get('naam')
            saverecord.email = request.POST.get('email')
            saverecord.onderwerp = request.POST.get('onderwerp')
            saverecord.bericht = request.POST.get('bericht')
            saverecord.save()
            messages.success(request, "Uw bericht is opgeslagen")
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')