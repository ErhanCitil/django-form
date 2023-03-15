from django.shortcuts import render
from .forms import ContactForm
from .models import Contactdata
from django.contrib import messages
from django.views.generic import FormView

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
    
class ContactForm(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
