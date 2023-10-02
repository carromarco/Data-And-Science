#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
datos_empleo = pd.read_csv("C:/Users/marco/Desktop/Desarrollos/Analisis y visualizacion de datos/ARCHIVOS/empleo.csv", encoding="latin-1")


# In[15]:


plt.figure(figsize=(12, 6))
plt.scatter(datos[datos['provincia'] == 'Buenos Aires']['mes'],
            datos[datos['provincia'] == 'Buenos Aires']['empleados_registrados_miles'],
            label='Buenos Aires', alpha=0.5)
plt.scatter(datos[datos['provincia'] == 'Capital Federal']['mes'],
            datos[datos['provincia'] == 'Capital Federal']['empleados_registrados_miles'],
            label='Capital Federal', alpha=0.5)
plt.xlabel('Fecha')
plt.ylabel('Empleados Registrados (Miles)')
plt.title('Comparación de Empleados Registrados entre Buenos Aires y CABA')
plt.legend()
plt.grid(True)


# In[ ]:




