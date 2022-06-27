from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .forms import SessionsForm
from .models import Barcode
import json

# Create your views here.
def home(req):
    issue_no = None
    form = SessionsForm()
    if req.method == "POST":
        form = SessionsForm(req.POST)
        if form.is_valid():
            form.save()
            issue_no = form.save().Issue_No

    return render(req, 'home.html', {'form': form, 'issue_no': issue_no})

def model_to_dic(model):
    dic={"message":"success"}
    dic["product_name"]=model.Name
    dic["item_number"]=model.Item_No
    dic["barcodenumber"]=model.Barcode_No
    return json.dumps(dic)

def get_info(request,id):
    
    ans=Barcode.objects.filter(Barcode_No=id)
    if(len(ans)==0):
        return HttpResponse('{"message":"No objects found"}',content_type='application/json')
    ans=model_to_dic(ans[0])

    return HttpResponse(ans,content_type='application/json')