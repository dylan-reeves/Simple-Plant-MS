from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import views, authenticate, login
from django.conf import settings
from .forms import loginForm

# Create your views here.
def login_view(request):
    nexturl =""
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
                if request.POST.get('netx') == "":
                    print('didnt find next')
                    request.user = user
                    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                else:
                    print('found next')
                    request.user = user
                    return HttpResponseRedirect(request.POST.get('next'))
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
        nexturl = request.GET['next']
        form = loginForm()
        return render(request, 'accounts/login.html', {'form': form,
                                                        'next': nexturl})
