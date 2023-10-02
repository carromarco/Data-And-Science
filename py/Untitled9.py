#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
datos_exportaciones = pd.read_csv("C:/Users/marco/Desktop/Desarrollos/Analisis y visualizacion de datos/ARCHIVOS/exportaciones.csv", encoding="latin-1")


# In[14]:


datos_total_pais = datos_exportaciones[(datos_exportaciones['provincia'] == 'Total País') & (datos_exportaciones['rubro'] == 'Total')]

plt.figure(figsize=(12, 6))
plt.bar(datos_total_pais['anio'], datos_total_pais['value'], label='Total País')
plt.xlabel('Año')
plt.ylabel('Total')
plt.title('Exportaciones')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




