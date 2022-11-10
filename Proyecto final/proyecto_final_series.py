# -*- coding: utf-8 -*-
"""proyecto final SERIES

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sWDWF65ya976cIp2-PMFX2L469whzO2F
"""

pip install transformers

import pandas as pd

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

from google.colab import files

uploaded = files.upload()

import io 
  
tv_show = pd.read_csv(io.BytesIO(uploaded['tv_shows_all.csv'])) 
tv_show

x = list(tv_show['all'])

x

y = [type(i) for i in x]



for i in x:
  if i is float:
    print(i)

y

for i in y:
  if i is float:
    print (i)

j = [i for i in x if isinstance(i, str)]

for i in x:
  if i is float:
    print (i)

po = classifier(j)

po

y = []
for element in po:
  x = element['label']
  y.append(x)

tv_show['sentiment'] = y

tv_show

tv_show.to_csv('tv_show_final.csv')

files.download('tv_show_final.csv')