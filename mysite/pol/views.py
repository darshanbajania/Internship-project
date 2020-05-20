from django.shortcuts import render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import random
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import pickle
import numpy as np
from nltk.corpus import stopwords 
import string
import re

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import collections
from . import kmeans
# Create your views here.
def home_view(request):
    #takes value from search
    text=request.POST.get('searches')
    disp_text=text
    kt=kmeans.kmean_categorize(disp_text)
    kcont={
        'km':kt,
    }
    w=""
    categ_str={
        'h':'',
        'string':disp_text
    }
    if text!=None:
        text=text.lower()
        #defining stopwords
        stop_words = set(stopwords.words('english'))
        symbols    = "!\"#$%&()*+-./:;<=>?@[\]^_`{|},~\n"
        
        #replacing spaces
        for i in symbols:
            text = np.char.replace(text, i, ' ')

        #replacing '
        text = np.char.replace(text, "'", "")   
        print(text)
        
        #converting to list
       
        text_list  = text.tolist()
        
        #splitting the text
        text_split=list(text_list.split(" "))
        print(text_split)
        
        #removing stopwords
        final_words=[]
        for word in text_split: 
            if word not in stop_words:
                final_words.append(word)  
        print(final_words)   
        
        #counting no of words
        words_count=collections.Counter(final_words)
        no_words=len(final_words)
        
        #calculating tf idf
        tf_idf={}
        for i in words_count:
            tf=words_count[i]/no_words
            df=1
            idf=np.log(1/df+1)
            tf_idf[i]=tf*idf
        
        #sorting tf idf words
        final_list=sorted(tf_idf, key=tf_idf.get, reverse=True)
        
        #making dictionary to create context
        top_words=final_list[:6]
        w=""
        for s in top_words:
            w=w+" "+s
        stop_words_set = set(stopwords.words('english'))#set of stopwords
        # print(kmean_categorize(w))
        



        k={}
        j=1
        for i in top_words:
            k[i]=j
            j=j+1


            
    else:
        a=2


    
    z=kmeans.kmean_categorize(w)
    cont={
        'm':z,
    }    
    print(z)
    return render(request,'pol/base.html',{'k':k,'cont':cont,'categ_str':categ_str,'kcont':kcont})