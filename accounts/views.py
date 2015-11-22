from django.shortcuts import render
from django.contrib.auth import views, authenticate, login
from .forms import loginForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = loginForm(request.POST)
        # check whether it's valid:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('user has been authenticated')
            if user.is_active:
                login(request,user)
                print('user has been logged in')
                if request.POST["next"] is Not "":
                    HttpResponseRedirect(request.POST["next"])
                else:
                    HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                print('user is not active')
                return HttpResponseRedirect('/accounts/deactivated/')
        else:
            print('incorrect logindetails')
            form = loginForm()
            return render(request, 'accounts/login.html', {'form': form,
                                                            'error': 'Incorrect User Details'} )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = loginForm()

    return render(request, 'accounts/login.html', {'form': form})
