from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import random
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
from kmeans import *
f = open(r'C:\Users\DARSHAN\p_category\mysite\pol\data.csv','r')
m = f.readlines()
text = []
label = [] 
for i in m:
   text.append(i[:-9])
   l = i[-13:].split(',')
   label.append(l[1])
preds = []
correct = 0.0
count = 0.0
for i in range(len(text)):
   pred = kmean_categorize(text[i])       
   preds.append(pred)
   if pred == label[i][:-1]:
      correct += 1
   count += 1
   print(i,pred,label[i],correct/count)