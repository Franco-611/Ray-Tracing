from ray import *

r = Raytracer(950, 450)

r.envmap = Envmap('fondo.bmp')
r.light = Light(V3(0, 0, 20), 2, color(255, 255, 255))
r.scene = [
    
    #///////////////ARBOLA/////////////////
    #tronco
    Cubo(V3(-10, 2, -15), 1, tronco),
    Cubo(V3(-10, 1, -15), 1, tronco),
    Cubo(V3(-10, 0, -15), 1, tronco),
    Cubo(V3(-10, -1, -15), 1, tronco),

    #fila 0
    Cubo(V3(-9.5, -1.8, -14), 1, hojas),
    Cubo(V3(-10.5, -1.8, -14), 1, hojas),
    Cubo(V3(-11.5, -1.8, -14), 1, hojas),
    Cubo(V3(-8.5, -1.8, -14), 1, hojas),

    Cubo(V3(-8.5, -1.8, -15), 1, hojas),
    Cubo(V3(-8.5, -1.8, -16), 1, hojas),

    Cubo(V3(-11.5, -1.8, -15), 1, hojas),
    Cubo(V3(-11.5, -1.8, -16), 1, hojas),

    Cubo(V3(-9.5, -1.8, -16), 1, hojas),
    Cubo(V3(-10.5, -1.8, -16), 1, hojas),
    Cubo(V3(-11.5, -1.8, -16), 1, hojas),
    Cubo(V3(-8.5, -1.8, -16), 1, hojas),

    #fila1 
    Cubo(V3(-9, -2.8, -14.5), 1, hojas),
    Cubo(V3(-10, -2.8, -14.5), 1, hojas),
    Cubo(V3(-11, -2.8, -14.5), 1, hojas),

    Cubo(V3(-9, -2.8, -15.5), 1, hojas),

    #fila0
    Cubo(V3(-10.25, -3.8, -15.5), 1, hojas),


    #///////////////ARBOLD/////////////////
    #tronco
    Cubo(V3(-10, 2, -10), 1, tronco),
    Cubo(V3(-10, 1, -10), 1, tronco),
    Cubo(V3(-10, 0, -10), 1, tronco),
    Cubo(V3(-10, -1, -10), 1, tronco),

    #fila 0
    Cubo(V3(-9.5, -1.8, -9), 1, hojas),
    Cubo(V3(-10.5, -1.8, -9), 1, hojas),
    Cubo(V3(-11.5, -1.8, -9), 1, hojas),
    Cubo(V3(-8.5, -1.8, -9), 1, hojas),

    Cubo(V3(-8.5, -1.8, -10), 1, hojas),
    Cubo(V3(-8.5, -1.8, -11), 1, hojas),

    Cubo(V3(-11.5, -1.8, -10), 1, hojas),
    Cubo(V3(-11.5, -1.8, -11), 1, hojas),

    Cubo(V3(-9.5, -1.8, -11), 1, hojas),
    Cubo(V3(-10.5, -1.8, -11), 1, hojas),
    Cubo(V3(-11.5, -1.8, -11), 1, hojas),
    Cubo(V3(-8.5, -1.8, -11), 1, hojas),

    #fila1 
    Cubo(V3(-9, -2.8, -9.5), 1, hojas),
    Cubo(V3(-10, -2.8, -9.5), 1, hojas),
    Cubo(V3(-11, -2.8, -9.5), 1, hojas),

    Cubo(V3(-9, -2.8, -10.5), 1, hojas),

    #fila0
    Cubo(V3(-10.25, -3.8, -10.5), 1, hojas),


    #///////////////ARBOLI/////////////////
    #tronco
    Cubo(V3(-4, 2, -10), 1, tronco),
    Cubo(V3(-4, 1, -10), 1, tronco),
    Cubo(V3(-4, 0, -10), 1, tronco),
    Cubo(V3(-4, -1, -10), 1, tronco),

    #fila 0
    Cubo(V3(-3.5, -1.8, -9), 1, hojas),
    Cubo(V3(-4.5, -1.8, -9), 1, hojas),
    Cubo(V3(-5.5, -1.8, -9), 1, hojas),
    Cubo(V3(-2.5, -1.8, -9), 1, hojas),

    Cubo(V3(-2.5, -1.8, -10), 1, hojas),
    Cubo(V3(-2.5, -1.8, -11), 1, hojas),

    Cubo(V3(-5.5, -1.8, -10), 1, hojas),
    Cubo(V3(-5.5, -1.8, -11), 1, hojas),

    Cubo(V3(-3.5, -1.8, -11), 1, hojas),
    Cubo(V3(-4.5, -1.8, -11), 1, hojas),
    Cubo(V3(-5.5, -1.8, -11), 1, hojas),
    Cubo(V3(-2.5, -1.8, -11), 1, hojas),

    #fila1 
    Cubo(V3(-3, -2.8, -9.5), 1, hojas),
    Cubo(V3(-4, -2.8, -9.5), 1, hojas),
    Cubo(V3(-5, -2.8, -9.5), 1, hojas),

    Cubo(V3(-3, -2.8, -10.5), 1, hojas),

    #fila0
    Cubo(V3(-4.25, -3.8, -10.5), 1, hojas),


    #Charco de agua
    Plane(V3(-7, 2.4, -12), 3, 8, agua),
    

    #Sphere(V3(0, 0, -9), 1, espejo),

    #///////////////CASA/////////////////
    #Columna izquierda
    Cubo(V3(7, 2, -25), 2.5, ladrillo),
    Cubo(V3(7, -0.5, -25), 2.5, ladrillo),
    Cubo(V3(7, -3, -25), 2.5, ladrillo),
    Cubo(V3(7, -5.5, -25), 2.5, ladrillo),
    #Columna derecha
    Cubo(V3(17, 2, -25), 2.5, ladrillo),
    Cubo(V3(17, -0.5, -25), 2.5, ladrillo),
    Cubo(V3(17, -3, -25), 2.5, ladrillo),
    Cubo(V3(17, -5.5, -25), 2.5, ladrillo),

    #Fila 3
    Cubo(V3(9.5, -5.5, -25), 2.5, ladrillo),
    Cubo(V3(12, -5.5, -25), 2.5, ladrillo),
    Cubo(V3(14.5, -5.5, -25), 2.5, ladrillo),
    #Fila 2
    Cubo(V3(9.5, -3, -25), 2.5, vidrio),
    Cubo(V3(12, -3, -25), 2.5, ladrillo),
    Cubo(V3(14.5, -3, -25), 2.5, puerta),
    #Fila 1
    Cubo(V3(9.5, -0.5, -25), 2.5, ladrillo),
    Cubo(V3(12, -0.5, -25), 2.5, ladrillo),
    Cubo(V3(14.5, -0.5, -25), 2.5, puerta),
    #Fila 0
    Cubo(V3(9.5, 2, -25), 2.5, ladrillo),
    Cubo(V3(12, 2, -25), 2.5, ladrillo),
    Cubo(V3(14.5, 2, -25), 2.5, puerta),


    #Techo
    Cubo(V3(6.5, -8, -24), 2.5, piedra),
    Cubo(V3(9, -8, -24), 2.5, piedra),
    Cubo(V3(11.5, -8, -24), 2.5, piedra),
    Cubo(V3(14, -8, -24), 2.5, piedra),
    Cubo(V3(16.5, -8, -24), 2.5, piedra),
    Cubo(V3(17, -8, -24), 2.5, piedra),

    Cubo(V3(6.5, -8, -26.5), 2.5, piedra),
    Cubo(V3(6.5, -8, -29), 2.5, piedra),
    Cubo(V3(6.5, -8, -31.5), 2.5, piedra),
    Cubo(V3(6.5, -8, -34), 2.5, piedra),
    Cubo(V3(6.5, -8, -36.5), 2.5, piedra),


    #Pared Derecha
    Cubo(V3(7, 2, -27.5), 2.5, ladrillo),
    Cubo(V3(7, -0.5, -27.5), 2.5, ladrillo),
    Cubo(V3(7, -3, -27.5), 2.5, vidrio),
    Cubo(V3(7, -5.5, -27.5), 2.5, ladrillo),

    Cubo(V3(7, 2, -30), 2.5, ladrillo),
    Cubo(V3(7, -0.5, -30), 2.5, ladrillo),
    Cubo(V3(7, -3, -30), 2.5, ladrillo),
    Cubo(V3(7, -5.5, -30), 2.5, ladrillo),

    Cubo(V3(7, 2, -32.5), 2.5, ladrillo),
    Cubo(V3(7, -0.5, -32.5), 2.5, ladrillo),
    Cubo(V3(7, -3, -32.5), 2.5, vidrio),
    Cubo(V3(7, -5.5, -32.5), 2.5, ladrillo),

    Cubo(V3(7, 2, -35), 2.5, ladrillo),
    Cubo(V3(7, -0.5, -35), 2.5, ladrillo),
    Cubo(V3(7, -3, -35), 2.5, ladrillo),
    Cubo(V3(7, -5.5, -35), 2.5, ladrillo),

    #pared fondo
    Cubo(V3(17, 2, -35), 2.5, ladrillo),
    Cubo(V3(17, -0.5, -35), 2.5, ladrillo),
    Cubo(V3(17, -3, -35), 2.5, ladrillo),
    Cubo(V3(17, -5.5, -35), 2.5, ladrillo),
    #Fila 3
    Cubo(V3(9.5, -5.5, -35), 2.5, ladrillo),
    Cubo(V3(12, -5.5, -35), 2.5, ladrillo),
    Cubo(V3(14.5, -5.5, -35), 2.5, ladrillo),
    #Fila 2
    Cubo(V3(9.5, -3, -35), 2.5, ladrillo),
    Cubo(V3(12, -3, -35), 2.5, ladrillo),
    Cubo(V3(14.5, -3, -35), 2.5, ladrillo),
    #Fila 1
    Cubo(V3(9.5, -0.5, -35), 2.5, ladrillo),
    Cubo(V3(12, -0.5, -35), 2.5, ladrillo),
    Cubo(V3(14.5, -0.5, -35), 2.5, ladrillo),
    #Fila 0
    Cubo(V3(9.5, 2, -35), 2.5, ladrillo),
    Cubo(V3(12, 2, -35), 2.5, ladrillo),
    Cubo(V3(14.5, 2, -35), 2.5, ladrillo),
    
]

r.render()
r.write('proyecto.bmp')