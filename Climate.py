#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv(r"C:\Learning\python_class\climate_data.csv")
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


a=df.groupby("Month").mean().reset_index()
a


# In[5]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
months=range(1,13)
plt.bar(months,a["Average temperature (°F)"],color="red")
plt.xlabel("Month",color="green")
plt.ylabel("Average temperature (°F)",color="green")
plt.show()


# In[6]:


import seaborn as sns

plt.figure(figsize=(10,6))
sns.barplot(a["Month"],a["Average temperature (°F)"])


# # Month With Highest Rainfall

# In[7]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
months=range(1,13)
plt.bar(months,a["Rainfall for month (in)"],color="red")
plt.xlabel("Month",color="green")
plt.ylabel("Rainfall for month (in)",color="green")
plt.show()


# In[8]:


import seaborn as sns

plt.figure(figsize=(10,6))
sns.barplot(a["Month"],a["Rainfall for month (in)"])


# In[9]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
months=range(1,13)
plt.bar(months,a["Maximum humidity (%)"],color="red")
plt.xlabel("Month",color="green")
plt.ylabel("Maximum humidity (%)",color="green")
plt.show()


# In[10]:


import seaborn as sns

plt.figure(figsize=(10,6))
sns.barplot(a["Month"],a["Maximum humidity (%)"])


# In[11]:


a.corr(method ='pearson')


# In[13]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(a)
plt.show()


# In[ ]:




