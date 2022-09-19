#%%
# Importamos las librerias para la serie de tiempo
from turtle import color
import pandas as pd
import plotnine
import math 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker ## Modifica las etquetas de los ejes

# Cargamos los precios históricos del petróleo 

datosP= pd.read_csv('/Datos históricos Futuros petróleo crudo WTI (2).csv', delimiter=',', decimal=',' )
print(datosP.head())

# Gráfica
plt.style.use('ggplot')
datosP.plot(x = 'Fecha', y =["Máximo", "Mínimo"],figsize= (18,14), color=['#1d37b9',"#b91da9"],)

# Estética  de la gráfica
plt.title(
    "En dólares por barril",
    fontname="Times New Roman",
    fontsize=14,
    pad=10,
)

plt.suptitle("Evolución del Precio del Petróleo WTI 2012-2022", fontsize=16,
    fontname="Times New Roman",
    fontweight="bold",
    x=0.126,
    y=0.96,
    ha="left",
)
plt.xlabel("Año",fontsize=20, fontweight="bold", fontname="Times New Roman")
plt.ylabel("Precio USD ($)", fontsize=20,fontname="Times New Roman", fontweight="bold")

# Muestra la gráfica
plt.show(block=True)
