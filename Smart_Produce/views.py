from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Dhrutika'})

def index(request):
    return render(request, 'index.html')


def add(request):
    val1 = request.POST['Name']

    return render(request, 'newlogin.html',{'Name':val1})
