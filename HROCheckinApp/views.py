from django.shortcuts import render, redirect
from django.http import HttpResponse
from HROCheckinApp.forms import StudentForm
from HROCheckinApp.models import Student

def home(request):
    return render(
        request,
        'HROCheckinApp/home.html'
	)

def login(request):
    form = StudentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            first_name = form.save(commit=False)
            first_name.save()
            return redirect("home")
        
    else:
        return render(request, "HROCheckinApp/login.html", {"Form": form})