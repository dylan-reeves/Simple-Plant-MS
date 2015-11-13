from django.shortcuts import render

# Create your views here.
def index(request):
    return render("index page")

def details(request):
    return render("details page")

def create(request):
    return render("Create Page")

def update(request):
    return render("Update Page")

def delete(request):
    return render("Delete Page")
