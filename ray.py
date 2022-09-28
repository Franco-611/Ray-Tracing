from turtle import position
from WriteUtilities import *
from math import *
from color import *
from vector import *
from sphere import *
from material import *
from light import *
import random

class Raytracer (object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.colorN = color(0, 0, 0) 
        self.colorD = color(0, 150, 150)
        self.scene = []
        self.light = Light(V3(0, 0, 0), 1) 
        self.density = 1
        self.clear()

    def point(self, x, y, c = None):
        if not (x >= self.width and x < 0 and y < 0 and y >= self.height):
            self.framebuffer[y][x]= c or self.colorD

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
        self.colorN = color

    def cambioD(self, color): 
        self.colorD = color

    def clear(self):
        self.framebuffer= [
            [self.colorN for x in range(self.width)]
            for y in range(self.height)
        ]

    def Color (self, r, g, b):
        self.colorD = color(r, g, b)

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

    def cast_ray (self, origin, direction):
        material, intersect = self.scene_intersect(origin, direction)

        if material is None:
            return self.colorD

        light_dir = (self.light.position - intersect.point).norm()
        intensity = light_dir @ intersect.normal

        if material:
            diffuse = color(
                int(material.diffuse[2] * intensity),
                int(material.diffuse[1] * intensity),
                int(material.diffuse[0] * intensity)
            )
            return diffuse
        else:
            return self.colorD

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


red = Material(diffuse=color(255, 0, 0))
white = Material(diffuse=color(255, 255, 255))

r = Raytracer(800, 600)
r.light = Light(V3(0, 0, 0), 1)
r.scene = [
    Sphere(V3(-3, 0, -16), 2.5, red),
    Sphere(V3(1, 0, -10), 2.5, white)
]
r.render()
r.write('render.bmp')