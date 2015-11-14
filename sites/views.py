from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import site

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'sites/index.html'
    context_object_name = 'site_list'
    def get_queryset(self):
        return site.objects.all()

class DetailView(generic.DetailView):
    model = site
    template_name = 'sites/details.html'

def create(request):
    return render("Create Page")

def update(request):
    return render("Update Page")

def delete(request):
    return render("Delete Page")
