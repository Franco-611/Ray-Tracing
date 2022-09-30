from ray import *

rubber = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1], spec=10)
ojos = Material(diffuse=color(255, 255, 255), albedo=[0.9, 0.1], spec=10)
ivory = Material(diffuse=color(100, 100, 80), albedo=[0.6, 0.3], spec=50)
az = Material(diffuse=color(0, 0, 255), albedo=[0.9, 0.1], spec=10)
r = Raytracer(800, 600)
r.cambioD(color(255,255,255))
r.light = Light(V3(0, 0, 0), 1.5, color(255, 255, 255))
r.scene = [
    #cuerpo
    Sphere(V3(0.1, 1, -10), 2, rubber),
    #cara
    Sphere(V3(0.1, -2, -10), 1.5, rubber),
    #manos
    Sphere(V3(-1.35, -0.2, -8), 0.5, rubber),
    Sphere(V3(1.55, -0.2, -8), 0.5, rubber),
    #pies
    Sphere(V3(-1.5, 2, -8), 0.68, rubber),
    Sphere(V3(1.55, 2, -8), 0.68, rubber),
    #orejas
    Sphere(V3(-0.8, -2.5, -8), 0.35, rubber),
    Sphere(V3(1, -2.5, -8), 0.35, rubber),
    #ojos
    Sphere(V3(-0.2, -1.3, -5), 0.08, ojos),
    Sphere(V3(0.3, -1.3, -5), 0.08, ojos),
    #nariz
    Sphere(V3(0.05, -0.85, -5), 0.25, ivory),


]
r.render()
r.write('RT2.bmp')