from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CheckBoxForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'info465/home.html')

def checkbox(request):
    if request.method == "POST":
        form = CheckBoxForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            statesVisited = form.cleaned_data['statesVisited']
            faveStateVisited = form.cleaned_data['faveStateVisited']
            comment = form.cleaned_data['comment']
            badweather = form.cleaned_data['badweather']
            faveColor = form.cleaned_data['faveColor']
            faveState = form.cleaned_data['faveState']
            messages.success(request, 'Profile details updated.')
            # return redirect('info465-test', {"form":form})
            return render(request, 'info465/test.html', {"form":form})

    else:
        form = CheckBoxForm()
        return render(request, 'info465/test.html', {"form":form})

def success(request):
    return render(request, 'info465/success.html')

def about(request):
    return render(request, 'info465/about.html')
