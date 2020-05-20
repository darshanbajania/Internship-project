# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:23:44 2020

@author: Mathew
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import pickle
import numpy as np
from nltk.corpus import stopwords 
import string
import re

stop_words_set = set(stopwords.words('english'))#set of stopwords

def clean_text (s,stop_words_set):
   s = s.lower()
   output = s.translate(str.maketrans('', '', string.punctuation))#remove punctuation
   output = re.sub(r'\d+', '',output)#remove digits
   temp = output.split(' ')
   output = ''
   for i in temp:#remove stopwords
      if i not in stop_words_set:
         output += i + ' '
   return output


def kmean_categorize(string = "no input!"):
   string = clean_text(string,stop_words_set)
   string = [string]#needs to be in list of str format
   categories = ['electronics','pets','home','clothing','toys']
   clusters = {0: 'nil',1: 'nil',2: 'nil',3: 'nil',4: 'nil'}
   vect = TfidfVectorizer(stop_words='english')
   with open('c:/Users/DARSHAN/Desktop/New_folder/kmeans.pkl', 'rb') as file:
      model = pickle.load(file)
      
   with open('c:/Users/DARSHAN/Desktop/New_folder/vect.pkl', 'rb') as file:
      vect = pickle.load(file)
   for i in categories:
      temp = vect.transform([i])
      temp_pred = model.predict(temp)
      clusters[temp_pred[0]] = i 
   y = vect.transform(string)
   pred = model.predict(y)
   return clusters[pred[0]]

