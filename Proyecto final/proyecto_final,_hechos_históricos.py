# -*- coding: utf-8 -*-
"""Proyecto final, hechos históricos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rz4WqfkEsVSzqQTvdwfM7VzuqJ2ey3hT
"""

pip install transformers

import pandas as pd

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

from google.colab import files

uploaded = files.upload()

import io 
  
events = pd.read_csv(io.BytesIO(uploaded['events_years.csv'])) 
events

x = list(events['Events'])

po = classifier(x)

po

y = []
for element in po:
  x = element['label']
  y.append(x)

events['sentiment'] = y

events

events.to_csv('events.csv')

files.download('events.csv')