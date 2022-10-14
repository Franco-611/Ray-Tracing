from plane import *
from material import *
from color import *

class Cubo(object):
    def __init__(self, center, tam, material): 
        self.tam = tam
        self.center = center
        self.material = material

    def ray_intersect(self, origin, direction):
        
        tmin = ((self.center.x - self.tam/2) - origin.x) / direction.x
        tmax = ((self.center.x + self.tam/2) - origin.x) / direction.x

        if tmin > tmax:
            tmin, tmax = tmax, tmin
        
        tymin = ((self.center.y - self.tam/2) - origin.y) / direction.y
        tymax = ((self.center.y + self.tam/2) - origin.y) / direction.y

        if tymin > tymax:
            tymin, tymax = tymax, tymin
        
        if tmin > tymax or tymin > tmax:
            return False
        
        if tymin > tmin:
            tmin = tymin
        
        if tymax < tmax:
            tmax = tymax

        tzmin = ((self.center.z - self.tam/2) - origin.z) / direction.z
        tzmax = ((self.center.z + self.tam/2) - origin.z) / direction.z

        if tzmin > tzmax:
            tzmin, tzmax = tzmax, tzmin
        
        if tmin > tzmax or tzmin > tmax:
            return False
        
        if tzmin > tmin:
            tmin = tzmin
        
        if tzmax < tmax:
            tmax = tzmax

        impact = origin + (direction * tmin)
        
        return Intersect(
            distance = tmin,
            point = impact,
            normal = V3(0, 1, 0)
        )
