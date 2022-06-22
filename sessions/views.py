from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SessionsForm

# Create your views here.
def home(req):
    submitted = False
    if req.method == "POST":
        form = SessionsForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')

    else:
        if 'submitted' in req.GET:
            submitted = True

    return render(req, 'home.html', {'form': SessionsForm})