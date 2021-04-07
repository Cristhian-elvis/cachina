from django.shortcuts import render

# Create your views here.

def signIn(request):

    return render(request, 'userApp/signIn.html')


def signUp(request):

    return render(request, 'userApp/signUp.html')
