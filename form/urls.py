from django.urls import path, include
from .views import insertdata, ContactForm

urlpatterns = [
    path('', insertdata, name='insertdata'),
    path('contact/', ContactForm.as_view(), name='contact'),
]