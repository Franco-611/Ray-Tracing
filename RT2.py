from ray import *

rubber = Material(diffuse=color(255, 50, 50), albedo=[0.6, 0.4], spec=8)
ojos = Material(diffuse=color(0, 0, 0), albedo=[0.9, 0.1], spec=5)
claro = Material(diffuse=color(255, 204, 153), albedo=[0.4, 0.6], spec=10)
madera = Material(diffuse=color(238, 225, 115), albedo=[0.9, 0.1], spec=245)

r = Raytracer(800, 600)
r.cambioD(color(209,178,123))
r.light = Light(V3(2, -2, 0), 2, color(255, 255, 255))
r.scene = [
    #cuerpo
    Sphere(V3(0.1, 1, -10), 2, rubber),
    #cara
    Sphere(V3(0.1, -2, -9.5), 1.5, madera),
    #manos
    Sphere(V3(-1.35, -0.2, -8), 0.5, madera),
    Sphere(V3(1.55, -0.2, -8), 0.5, madera),
    #pies
    Sphere(V3(-1.5, 2, -8), 0.68, madera),
    Sphere(V3(1.55, 2, -8), 0.68, madera),
    #orejas
    Sphere(V3(-0.8, -2.8, -8), 0.35, madera),
    Sphere(V3(0.95, -2.8, -8), 0.35, madera),
    #ojos
    Sphere(V3(-0.2, -1.3, -5), 0.08, ojos),
    Sphere(V3(0.3, -1.3, -5), 0.08, ojos),
    #nariz
    Sphere(V3(0.05, -0.85, -5), 0.25, claro),


]
r.render()
r.write('RT2.bmp')