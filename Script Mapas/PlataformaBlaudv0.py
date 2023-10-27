from flask import Flask, render_template_string
import webbrowser  # website
import numpy as np # numpy
import ee # Earth Engine
from eeconvert import eeImageToFoliumLayer as ee_plot # eeconvert
import folium # Plugins
from folium.plugins import Draw
from folium.plugins import MousePosition
from folium.plugins import HeatMap
from datetime import datetime, timedelta

coordenada_centrar=[7.570475, -74.400856]

try:
    ee.Initialize()
    print("El paquete EE inicio satisfactoriamente")
except ee.EEException as e:
    print('Paquete EE fallo para iniciar')
except:
    print("error inesperado", sys.exc_info()[0])
    raise
# procesamiento de datos para heatmap
np.random.seed(3141592)
initial_data = np.random.normal(size=(100, 2)) * np.array([[1, 1]]) + np.array([[coordenada_centrar[0],coordenada_centrar[1]]]
)

move_data = np.random.normal(size=(100, 2)) * 0.01

data = [(initial_data + move_data * i).tolist() for i in range(100)]


#animacion de mapa de calor
time_index = [(datetime.now() + k * timedelta(1)).strftime("%Y-%m-%d") for k in range(len(data))
              ]

m = folium.Map(
    location=coordenada_centrar,
    width='100%',
    height='50%',
    tiles = 'stamentoner',
    zoom_start=7
    );

#plugins
folium.plugins.Geocoder().add_to(m)
MousePosition().add_to(m)
Draw(export=True).add_to(m)
hm = folium.plugins.HeatMapWithTime(data, index=time_index, auto_play=True, max_opacity=.3)

hm.add_to(m)
#HeatMap(data).add_to(m)
#
feature_group = folium.FeatureGroup(name="Mapa")
folium.Marker(location=coordenada_centrar).add_to(feature_group)
m.add_child(feature_group)
m.add_child(folium.map.LayerControl())


#Cargar Pagina
archivoHtml='SolarScout.html';
m.save(archivoHtml)
webbrowser.open(archivoHtml)