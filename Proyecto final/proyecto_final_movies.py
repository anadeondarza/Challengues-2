# -*- coding: utf-8 -*-
"""Proyecto final - movies

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RV5aqTh6fImGjrJL2HzhbY-G1nzb6nUS
"""

pip install transformers

import pandas as pd

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

re = classifier("I have been waiting for a hug")

print(re)

from google.colab import files

uploaded = files.upload()

import io 
  
movies = pd.read_csv(io.BytesIO(uploaded['movies_1.csv'])) 
movies



x = list(movies['description'])

print(type(x))

po = classifier(x)

po

y = []
for element in po:
  x = element['label']
  y.append(x)

y

movies['sentiment'] = y

movies

x = movies['sentiment'].unique()
x