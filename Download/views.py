from django.shortcuts import render
from .models import Apps

# Create your views here.

def index(request):
    apps = Apps.objects.all()
    company_name = "Swoop"
    title = "Download Swoop Apps"
    company_email = "ceo@cydromeda.cf"
    return render(request, 'index.html', {'apps': apps, 'company_name': company_name, 'company_email': company_email, 'title': title})
    
def detail(request, product_name):
    app = Apps.objects.get(Name=product_name)
    company_name = "Swoop"
    title = "Download " + app.Name
    company_email = "ceo@cydromeda.cf"
    return render(request, 'detail.html', {'app': app, 'company_name': company_name, 'company_email': company_email, 'title': title})
