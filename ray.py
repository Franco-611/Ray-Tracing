from WriteUtilities import *
from math import *
from color import *
from cubo import Cubo
from vector import *
from sphere import *
from material import *
from light import *
from plane import *
from mats import *
from envmap import *
import random

MAX_RECURCIO = 3

class Raytracer (object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.colorN = color(0, 0, 100)
        self.colorD = color(0, 0, 100)
        self.scene = []
        self.light = Light(V3(0, 0, 0), 1, color(255, 255, 255))
        self.density = 1
        self.envmap = None
        self.clear()

    def point(self, x, y, c = None):
        if not (x >= self.width and x < 0 and y < 0 and y >= self.height):
            self.framebuffer[y][x]= c.to_bytes() or self.colorD.to_bytes()

    def write(self, filename="r.bmp"):
        f= open(filename, 'bw')

        offset = (4 - (self.width * 3) % 4) % 4
        new_width = offset + self.width

        # pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + new_width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        # info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        extra_bytes = [0, 0, 0]
        # pixel data
        for y in range(self.height):
            for x in range(self.width):
                if y < self.height and x < self.width:
                    f.write(self.framebuffer[y][x])
            f.write(bytes(extra_bytes[0:offset]))

        f.close()

    def cambioN(self, color): 
        self.colorN = color.to_bytes()

    def cambioD(self, color): 
        self.colorD = color.to_bytes()

    def clear(self):
        self.framebuffer= [
            [self.colorN.to_bytes() for x in range(self.width)]
            for y in range(self.height)
        ]

    def Color (self, r, g, b):
        self.colorD = color(r, g, b).to_bytes()

    def render (self):
        fov = int(pi/2)
        ar = self.width / self.height
        tana = tan(fov/2)

        for y in range(self.height):
            for x in range(self.width):
                if random.random() < self.density:

                    i = ((2 * (x + 0.5) / self.width) - 1) * ar * tana
                    j = (1 - (2 * (y + 0.5) / self.height)) * tana
                    
                    direction = V3(i, j, -1).norm()
                    origin = V3(0, 0, 0)
                    c = self.cast_ray(origin, direction)

                    self.point(x, y, c)

    def cast_ray (self, origin, direction, recursion = 0):

        if recursion >= MAX_RECURCIO:
            return self.get_background(direction)

        material, intersect = self.scene_intersect(origin, direction)

        if material is None:
            return self.get_background(direction)

        light_dir = (self.light.position - intersect.point).norm()
        

        reflected_color = color(0,0,0,)
        if material.albedo[2] > 0:
            reversed_direction = direction * -1
            reflected_direction = self.reflect(direction, intersect.normal)
            reflected_bias = -0.5 if reflected_direction @ intersect.normal < 0 else 0.5
            reflected_orig = intersect.point + (intersect.normal * reflected_bias)
            reflected_color = self.cast_ray(reflected_orig, reflected_direction, recursion + 1)

        refract_color = color(0,0,0,)
        if material.albedo[3] > 0:
            refract_direction = self.refract(direction, intersect.normal, material.refraction)
            refract_bias = -0.5 if refract_direction @ intersect.normal < 0 else 0.5
            refract_orig = intersect.point + (intersect.normal * refract_bias)
            refract_color = self.cast_ray(refract_orig, refract_direction, recursion + 1)
            

        reflection = reflected_color * material.albedo[2]

        refract = refract_color * material.albedo[3]

        deffuse_intensity = light_dir @ intersect.normal
        
        light_reflection = self.reflect(light_dir, intersect.normal)
        reflection_intensity = max(0, (light_reflection @ direction))
        specular_intensity =  reflection_intensity ** material.spec

        shadow_bias = 1.1
        shadow_orig = intersect.point + (intersect.normal * shadow_bias)
        shadow_material, shadow_intersect = self.scene_intersect(shadow_orig, light_dir)
        shadow_intensity = 1


        if shadow_material:
            shadow_intensity = 0.3

        specular = self.light.c * specular_intensity * material.albedo[1] * self.light.intensity

        diffuse = material.diffuse * deffuse_intensity * material.albedo[0] * shadow_intensity
        diffuse = diffuse + specular + reflection + refract

    
        return diffuse

    def scene_intersect (self, origin, direction):
        zbuffer = 999999
        material = None
        intersect = None

        for s in self.scene:
            object_intersect = s.ray_intersect(origin, direction)
            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer = object_intersect.distance
                    material = s.material
                    intersect = object_intersect

        return material, intersect

    def reflect(self, I, N):
        return (I - N * 2 * (N @ I)).norm()

    def refract(self, I, N, roi):
        etai = 1 #para el aire
        etat = roi

        cosi = (I @ N)* -1

        if cosi < 0:
            cosi *= -1
            etai *= -1
            etat *= -1
            N *= -1
        
        eta = etai/etat
        k = 1 - eta**2 * (1 - cosi**2)

        if k < 0:
            return V3(0,0,0)

        cost = k ** 0.5
        return ((I * eta) +  (N * (eta * cosi - cost))).norm() 

    def get_background(self,direction):
        if self.envmap:
            return self.envmap.get_color(direction)
        else:
            return self.colorD

r = Raytracer(950, 450)

'''
r.light = Light(V3(0, 0, 0), 1.5, color(255, 255, 255))
r.scene = [
    Sphere(V3(-6, 0, -16), 2.5, mirror),
    Sphere(V3(1, 0, -10), 2.5, ivory)
]
'''
r.envmap = Envmap('fondo.bmp')
r.light = Light(V3(-20, 20, 20), 2, color(255, 255, 255))
r.scene = [
    #Plane(V3(0, 2.2, -5), 2, 2, mirror),
    #Sphere(V3(0, -1.5, -10), 1.5, ivory),
    #Sphere(V3(0, 0, -5), 0.5, glass),
    #Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(2, 1, -10), 1, mirror),
    Cubo(V3(-2, 2, -10), 1.5, mirror),
]

r.render()
r.write('render.bmp')