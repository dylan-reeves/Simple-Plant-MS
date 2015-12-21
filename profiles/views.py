from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views import generic

from . import models

class IndexView(gene.ListView):
    model = userProfile
    template_name = 'profiles/index.html'
    context_object_name = 'profile_list'

class DetailView(generic.DeleteView):
    model = userProfile
    template_name = 'profiles/details.html'
    context_object_name = 'profile_details'

class CreateView(generic.CreateView):
    model = userProfile
