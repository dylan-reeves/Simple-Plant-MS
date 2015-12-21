from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views import generic

from . import models

class IndexView(generic.ListView):
    model = models.userProfile
    template_name = 'profiles/index.html'
    context_object_name = 'profile_list'

class DetailView(generic.DeleteView):
    model = models.userProfile
    template_name = 'profiles/details.html'
    context_object_name = 'profile_details'

class CreateView(generic.CreateView):
    model = models.userProfile
    template_name = 'profiles/create.html'
    context_object_name = 'profile_details'
    success_url = '/profiles/'

class UpdateView(generic.UpdateView):
    model = models.userProfile
    template_name = 'profiles/update.html'
    context_object_name = 'profile_details'
    success_url = '/profiles/'

class DeleteView(generic.DeleteView):
    model = models.userProfile
    template_name = 'profiles/delete.html'
    success_url = '/profiles/'
