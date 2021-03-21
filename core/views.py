from django.shortcuts import render
from .models import Women, Men, Couple
from about.models import About

# Create your views here.

def index(request):
    women= Women.objects.all()
    men = Men.objects.all()
    couples = Couple.objects.all()
    abouts = About.objects.all()
    return render(request, 'core/index.html', {'women':women, 'men':men, 'couples': couples, 'abouts':abouts})