from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            return redirect("accounts:login")
    else:
        form =RegisterForm()
    return render(request,"signup.html",{"form":form})
