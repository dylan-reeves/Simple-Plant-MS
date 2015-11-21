from django.shortcuts import render
from django.contrib.auth import views
from .forms import loginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = loginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/sites/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = loginForm()

    return render(request, 'accounts/login.html', {'form': form})
