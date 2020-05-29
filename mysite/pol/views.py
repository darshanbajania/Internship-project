from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import BookForm,ProposalForm, UserUpdateForm, ProfileUpdateForm
from .models import Book
from .models import Proposal,profile
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from sklearn.cluster import KMeans
import pandas as pd
import pickle
import numpy as np
import string
import re
from . import categorize
import collections
import random
from . import kmeans


# Create your views here.

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    
    return render(request, 'pol/upload.html',context)

def book_list(request):
    books = Book.objects.all()
    return render(request,'pol/book_list.html',{
        'books':books
    })

def Upload_book(request):
    form = ProposalForm()
    if request.method == 'POST':
        form = ProposalForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('pol:dashboard')
        else:
            form = ProposalForm(instance=request.user.profile)

    return render(request,'pol/Upload_book.html',{'form':form})



def index_view(request):
    return render(request,'pol/index.html')
    
def home_view(request):
    #takes value from search
    text=request.POST.get('searches')
    
    disp_text=text
    k={}
    [k,w]=categorize.categorize_idf(disp_text)
    wt=w
    if disp_text!=None:
        kt=kmeans.kmean_categorize(disp_text)
        kcont = {
            'km':kt,
        }
    else:
        kcont = {
            'km':"  "
        }
    
    categ_str = {
        'h':'',
        'string':disp_text,
    }
    z = kmeans.kmean_categorize(wt)
    cont = {
        'm':z,
    }    
    #print(z)
    return render(request, 'pol/base.html', {'k': k,'cont' : cont, 
    'categ_str' : categ_str, 'kcont' : kcont})

def Resource_View(request):
    return render(request,'pol/resources.html')


@login_required

def Profile_View(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('pol:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'pol/profile.html',context)

def dashboard_view(request):       #for dashboard
    prop = ProposalForm(instance=request.user.profile)
    return render(request,'pol/dashboard.html',{'prop':prop})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pol:login_urls')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

