from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import siteForm

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
    context_object_name = 'site_details'

class CreateView(generic.View):
    def get(self, request):
        form = siteForm
        return render(request, 'sites/create.html', {'form': form})
    def post(self, request):
        form = siteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

def update(request):
    return render("Update Page")

class DeleteView(generic.View):
    def get(self,request):
        
    return render("Delete Page")
