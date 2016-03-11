from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

# def index(request):
#     return HttpResponse("Hello, world.")

def index(request):
    return render(request, 'ideas/index.html')

# class IndexView(DetailView):
#     template_name = "ideas/index.html"

