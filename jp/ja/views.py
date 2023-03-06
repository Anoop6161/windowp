from django.shortcuts import render
from django.views.generic import TemplateView

class aboutview(TemplateView):
    template_name = ('about.html')

class HomeView(TemplateView):
    template_name = ('home.html')

class Contactus(TemplateView) :
    template_name = ('contact.html')
class Property(TemplateView) :
    template_name = ('property.html')

class PriceView(TemplateView) :
    template_name = ('price.html')

class UserPage(TemplateView) :
    template_name = ('userp.html')

class Recommond(TemplateView) :
    template_name = ('recomonded.html')



# Create your views here.
