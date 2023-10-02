#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
datos_empleo = pd.read_csv("C:/Users/marco/Desktop/Desarrollos/Analisis y visualizacion de datos/ARCHIVOS/empleo.csv", encoding="latin-1")


# In[59]:


buenos_aires_datos = datos_empleo[datos_empleo['provincia'] == 'Buenos Aires']
plt.figure(figsize=(10, 6))
plt.bar(datos_empleo['anio'], datos_empleo['empleados_registrados_miles'], color='blue')
plt.xlabel('año')
plt.ylabel('empleados registrados cada 100 mil hab')
plt.grid('True')
plt.tight_layout()
plt.show()


# In[60]:


plt.bar(pivot_table.index, pivot_table['Capital Federal'], label='Capital Federal', width=20, bottom=pivot_table['Buenos Aires'])
plt.xlabel('Fecha')
plt.ylabel('Empleados Registrados (Miles)')
plt.title('Relación entre Empleados Registrados en Buenos Aires y CABA')
plt.legend()
plt.grid(True)


# In[ ]:




