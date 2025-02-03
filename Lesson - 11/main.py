import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data=pd.read_csv('penguins_size.csv')
print(data.head())
print(data.head(15))
print(data.info())

data['sex']=data['sex'].map({'unknown':0,'FEMALE':1,"MALE":2,}).astype(int)
print(data.head())

greph=pd.DataFrame(data.groupby("sex")['flipper_length'].sum())
grephh=px.scatter('')