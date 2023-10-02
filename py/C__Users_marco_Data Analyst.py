#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import os
import matplotlib as plt
poblacion_df = pd.read_csv("C:/Users/marco/Desktop/Desarrollos/Analisis y visualizacion de datos/ARCHIVOS/poblacion.csv", encoding = "latin-1 ")
hogares_viviendas_df = pd.read_csv("C:/Users/marco/Desktop/Desarrollos/Analisis y visualizacion de datos/ARCHIVOS/hogares_viviendas_superficie.csv", encoding = "latin-1")
poblacion_df


# In[9]:


poblacion_df = poblacion_df[poblacion_df['provincia'] != 'Total Pais']
poblacion_df


# In[11]:


poblacion_df_densidad = pd.merge(poblacion_df, hogares_viviendas_df, left_on = ["provincia"], right_on = ["provincia"], how = 'left')
poblacion_df_densidad


# In[13]:


poblacion_df_densidad_sin_nan = poblacion_df_densidad.dropna()
c


# In[14]:





# In[15]:


poblacion_df_densidad


# In[16]:


poblacion_df_densidad['densidad_poblacional'] = poblacion_df_densidad['poblacion_total'] / poblacion_df_densidad['superficie_km2']
poblacion_df_densidad


# In[17]:


poblacion_df_densidad_sin_nan = poblacion_df_densidad.dropna()


# In[18]:


poblacion_df_densidad_sin_nan


# In[19]:


poblacion_df_densidad_sin_nan['densidad_poblacional'].describe()


# In[20]:


poblacion_df_densidad_sin_nan['hogares'].describe()


# In[21]:


poblacion_df


# In[23]:


poblacion_df['poblacion_total'].describe()


# In[ ]:




