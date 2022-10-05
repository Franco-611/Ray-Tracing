from turtle import position

import scipy as sp
from WriteUtilities import *
from math import *
from color import *
from vector import *
from sphere import *
from material import *
from light import *
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
            return self.colorD

        material, intersect = self.scene_intersect(origin, direction)

        if material is None:
            return self.colorD

        light_dir = (self.light.position - intersect.point).norm()
        

        reflected_color = color(0,0,0,)
        if material.albedo[2] > 0:
            reversed_direction = direction * -1
            reflected_direction = self.reflect(reversed_direction, intersect.normal)
            reflected_bias = -0.5 if reflected_direction @ intersect.normal < 0 else 0.5
            reflected_orig = intersect.point + (intersect.normal * reflected_bias)
            reflected_color = self.cast_ray(reflected_orig, reflected_direction, recursion + 1)
            

        reflection = reflected_color * material.albedo[2]

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
        diffuse = diffuse + specular + reflection

    
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



rubber = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0], spec=10)
ivory = Material(diffuse=color(100, 100, 80), albedo=[0.6, 0.3,0], spec=50)
mirror = Material(diffuse=color(255,255, 255), albedo=[0, 1, 0.8], spec=1425)

r = Raytracer(800, 600)

'''
r.light = Light(V3(0, 0, 0), 1.5, color(255, 255, 255))
r.scene = [
    Sphere(V3(-6, 0, -16), 2.5, mirror),
    Sphere(V3(1, 0, -10), 2.5, ivory)
]
'''

r.light = Light(V3(-20, 20, 20), 2, color(255, 255, 255))
r.scene = [
    Sphere(V3(0, -1.5, -12), 1.5, ivory),
    #Sphere(V3(-2, -1, -12), 2, mirror),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-2, 1, -10), 2, mirror),
]

r.render()
r.write('render.bmp')