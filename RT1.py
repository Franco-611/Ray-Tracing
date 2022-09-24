from ray import *

r = Raytracer(800,600)
#r.cambioN(color(0, 255, 255))
#r.cambioD(color(0, 255, 255))
r.clear()
r.scene = [
    Sphere(V3(-0.3, -4.2, -15), 0.15, color(0, 0, 0)),
    Sphere(V3(0.5, -4.2, -15), 0.15, color(0, 0, 0)),
    Sphere(V3(-0.3, -3.4, -15), 0.07, color(0, 0, 0)),
    Sphere(V3(-0.1, -3.3, -15), 0.07, color(0, 0, 0)),
    Sphere(V3(0.1, -3.3, -15), 0.07, color(0, 0, 0)),
    Sphere(V3(0.3, -3.3, -15), 0.07, color(0, 0, 0)),
    Sphere(V3(0.5, -3.4, -15), 0.07, color(0, 0, 0)),
    Sphere(V3(0.1, -3.7, -15), 0.15, color(255, 190, 9)),
    Sphere(V3(0.1, -1, -15), 0.17, color(0, 0, 0)),
    Sphere(V3(0.1, 1.5, -15), 0.17, color(0, 0, 0)),
    Sphere(V3(0.1, 0.1, -15), 0.17, color(0, 0, 0)),
    Sphere(V3(0.1, 3.4, -15), 3, color(255, 255, 255)), 
    Sphere(V3(0.1, -1, -15), 2, color(255, 255, 255)),
    Sphere(V3(0.1, -4, -15), 1.3, color(255, 255, 255))
]
r.render()
r.write('RT1.bmp')