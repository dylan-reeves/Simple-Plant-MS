from django.shortcuts import render
from django.contrib.auth import views, authenticate, login
from .forms import loginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = loginForm(request.POST)
        # check whether it's valid:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/accounts/success/')
            else:
                return HttpResponseRedirect('/accounts/deactivated/')
        else:
            form = loginForm()
            return render(request, 'accounts/login.html', {'form': form,
                                                            'error': 'Incorrect User Details'} )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = loginForm()

    return render(request, 'accounts/login.html', {'form': form})
