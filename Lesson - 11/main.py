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
grephh==px.scatter(greph,x=greph.index,y='flipper_length',size='flipper_length',size_max=100,color=greph.index,title="flipper length bigger in male or femal")
grephh.write_html('flipper_lengths.html',auto_open=True)
