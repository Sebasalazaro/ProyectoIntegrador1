from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    ##return HttpResponse('<h1>Welcome to Home Page</1>')
    ##return render(request, 'home.html')
    ##return render(request, 'home.html', {'name':'Sebastian Salazar'})

    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm':searchTerm})

def about(request):
    return render(request, 'about.html')

# Create your views here.
