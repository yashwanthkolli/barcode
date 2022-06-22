from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SessionsForm

# Create your views here.
def home(req):
    issue_no = None
    submitted = False
    form = SessionsForm()
    if req.method == "POST":
        form = SessionsForm(req.POST)
        if form.is_valid():
            form.save()
            issue_no = form.save().Issue_No

    return render(req, 'home.html', {'form': form, 'issue_no': issue_no})