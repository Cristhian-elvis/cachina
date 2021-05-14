from django.shortcuts import render, HttpResponse

from django.http import HttpResponseRedirect
from .forms import UserRegister
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def authentication(request):
    user = authenticate(
                request=request,
                username=request.POST['username'],
                password=request.POST['password1']
            )
    return user

def signIn(request):

    if request.method == 'POST':
            user = authentication(request)
            #txt = request.POST['email'] + " / "+ request.POST['password']
            #return HttpResponse("login: "+txt)
            if user is not None:
                login(request, user)
                #return HttpResponse("Logueado")
                return HttpResponseRedirect(reverse('Home'))
        
    return render(request, 'userApp/signIn.html')


def signUp(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegister(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            
            form.save()

            login(request, authentication(request))

            #nombre = form.cleaned_data['username']
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('Home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserRegister()
    return render(request, 'userApp/signUp.html', {'form': form})

def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))
