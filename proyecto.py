from ray import *

r = Raytracer(950, 450)

r.envmap = Envmap('fondo.bmp')
r.light = Light(V3(-10, 0, 20), 2, color(255, 255, 255))
r.scene = [

    #Cubo(V3(8, 4.6, -20), 1.3, tierra),
    #Cubo(V3(8, 3.3, -20), 1.3, piedra),
    #Cubo(V3(8, 2, -20), 1.3, ladrillo),
    #Plane(V3(0, 2.2, -5), 2, 2, espejo),

    
    #Cubo(V3(0, 5, -20), 4, agua)
    #Plane(V3(0, 2.2, -7), 2, 2, espejo),
    Sphere(V3(0, 0, -9), 1, espejo),

    Plane(V3(0, 2, -5.2), 2, 2, agua),
    #Cubo(V3(-1, 1, -6), 1.5, ladrillo),

    
]

r.render()
r.write('proyecto.bmp')