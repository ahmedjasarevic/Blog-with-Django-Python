from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"{single_slug} is a category")

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"{single_slug} is a category")

    return HttpResponse(f"{single_slug} does not correspond to anything")



def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories":TutorialCategory.objects.all})
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account Created:{username}" )
            login(request, user)
            messages.info(request, f"You are now logged in as: {username}")
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")


    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Loggeout out successfully")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as: {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username of password")

    else:
                messages.error(request, "Invalid username of password")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                {"form":form})
