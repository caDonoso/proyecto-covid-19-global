#!/usr/bin/env python
# coding: utf-8

# In[102]:


import pandas as pd

df=pd.read_csv('owid-covid-data.csv')

# Filter null data
filter = (df['iso_code'] != 'OWID_WRL') & (pd.notnull(df['iso_code'])) & (pd.notnull(df['total_cases']))
df = df[filter]

# Filter by country
#countries = ['USA', 'BR', 'IN']
#filter = df['iso_code'].isin(countries)
#df = df[filter]

# Filter by date
filter = df['date'] == '2020-07-31'
df = df[filter]
global_sum = df.sum(axis=0)

global_cases = global_sum['total_cases']
global_deaths = global_sum['total_deaths']

#extract from https://news.google.com/covid19/map?hl=es-419&gl=US&ceid=US%3Aes-419
global_recovered = 10155026 


ranking_cases = df[filter].nlargest(10, ['total_cases']) 

# Add recovered from https://news.google.com/covid19/map?hl=es-419&gl=US&ceid=US%3Aes-419 ordered by country
ranking_cases.insert(7, 'total_recovered', [2241632, 1824095, 1057805, 638410, 309601, 272187, 283915, 328327, 1438, 263519])


# In[90]:


import matplotlib.pyplot as plt


# In[108]:


# Continente Norte america
north_america = ranking_cases[ranking_cases['continent'] == 'North America']
north_america_columns_sum = north_america.sum(axis=0)

north_america_total_cases = north_america_columns_sum['total_cases']
north_america_total_deaths = north_america_columns_sum['total_deaths']
north_america_total_recovered = north_america_columns_sum['total_recovered']


# In[109]:


# Continente Sur america
south_america = ranking_cases[ranking_cases['continent'] == 'South America']
south_america_columns_sum = south_america.sum(axis=0)

south_america_total_cases = south_america_columns_sum['total_cases']
south_america_total_deaths = south_america_columns_sum['total_deaths']
south_america_total_recovered = south_america_columns_sum['total_recovered']


# In[110]:


# Continente Asia
asia = ranking_cases[ranking_cases['continent'] == 'Asia']
asia_columns_sum = asia.sum(axis=0)

asia_total_cases = asia_columns_sum['total_cases']
asia_total_deaths = asia_columns_sum['total_deaths']
asia_total_recovered = asia_columns_sum['total_recovered']


# In[111]:


# Continente Europa
europe = ranking_cases[ranking_cases['continent'] == 'Europe']
europe_columns_sum = europe.sum(axis=0)

europe_total_cases = europe_columns_sum['total_cases']
europe_total_deaths = europe_columns_sum['total_deaths']
europe_total_recovered = europe_columns_sum['total_recovered']


# In[112]:


# Continente Africa
africa = ranking_cases[ranking_cases['continent'] == 'Africa']
africa_columns_sum = africa.sum(axis=0)

africa_total_cases = africa_columns_sum['total_cases']
africa_total_deaths = africa_columns_sum['total_deaths']
africa_total_recovered = africa_columns_sum['total_recovered']

# In[113]:
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Casos Totales', 'Muertes totales', 'Recuperados totales']
sizes = [(africa.iloc[0,4]),(africa.iloc[0,6]), (africa.iloc[0,7])]


fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Continente africano')

plt.show()

# In[114]:
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Casos Totales', 'Muertes totales', 'Recuperados totales']
sizes = [asia_total_cases,asia_total_deaths, asia_total_recovered]


fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Continente Asiatico')

plt.show()
# In[115]:
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Casos Totales', 'Muertes totales', 'Recuperados totales']
sizes = [europe_total_cases, europe_total_deaths, europe_total_recovered]


fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Continente europeo')

plt.show()
# In[116]:
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Casos Totales', 'Muertes totales', 'Recuperados totales']
sizes = [(north_america_total_cases),(north_america_total_deaths), (north_america_total_recovered)]


fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Norte America')

plt.show()
# In[117]:
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Casos Totales', 'Muertes totales', 'Recuperados totales']
sizes = [south_america_total_cases,south_america_total_deaths, (south_america_total_recovered)]


fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Sudamerica')
# In[118]:
import numpy as np
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Casos Totales', 'Muertes totales', 'Recuperados totales']
sizes = [global_cases,global_deaths,global_recovered ]


fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Casos a nivel mundial')