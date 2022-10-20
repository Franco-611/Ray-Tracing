from material import *
from color import *
from texture import *

manzana = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10)
espejo = Material(diffuse=color(255,255, 255), albedo=[0, 1, 0.8,0], spec=1425)
agua = Material(diffuse=color(0, 0, 200), albedo=[0, 0.5,0.35,0.8], spec=90, refraction=1)
vidrio = Material(diffuse=color(150,180, 200), albedo=[0, 0.5, 0.1, 0.8], spec=125, refraction=1.5)
madera = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10, texture= Textures('madera.bmp'))
hojas = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10, texture= Textures('hojas.bmp'))
arbol = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10, texture= Textures('tronco.bmp'))
tierra = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10, texture= Textures('tierra.bmp'))
piedra = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10, texture= Textures('piedra.bmp'))
ladrillo = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10, texture= Textures('ladrillo.bmp'))