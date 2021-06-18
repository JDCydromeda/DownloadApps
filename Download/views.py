from django.shortcuts import render
from .models import Apps

# Create your views here.

def index(request):
    company_name = "Swoop"
    title = "Download Swoop Apps"
    company_email = "ceo@cydromeda.cf"
    return render(request, 'index.html', {'apps': Apps.objects.all(), 'company_name': company_name, 'company_email': company_email, 'title': title})
    

