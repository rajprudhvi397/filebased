from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

@cache_page(25)
def home(request):
    print('hii')
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')