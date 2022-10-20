from plane import *
from material import *
from color import *

class Cubo(object):
    def __init__(self, center, tam, material): 
        self.w = tam
        self.center = center
        self.material = material

    def ray_intersect(self, origin, direction):

            min = V3((self.center.x - self.w/2), (self.center.y - self.w/2), (self.center.z - self.w/2))
            max = V3((self.center.x + self.w/2), (self.center.y + self.w/2), (self.center.z + self.w/2))
            porcent = (0,0)
            
            tmin = ((self.center.x - self.w/2) - origin.x) / direction.x
            tmax = ((self.center.x + self.w/2) - origin.x) / direction.x

            if tmin > tmax:
                tmin, tmax = tmax, tmin
            
            tymin = ((self.center.y - self.w/2) - origin.y) / direction.y
            tymax = ((self.center.y + self.w/2) - origin.y) / direction.y

            if tymin > tymax:
                tymin, tymax = tymax, tymin
            
            if tmin > tymax or tymin > tmax:
                return False
            
            if tymin > tmin:
                tmin = tymin
            
            if tymax < tmax:
                tmax = tymax

            tzmin = ((self.center.z - self.w/2) - origin.z) / direction.z
            tzmax = ((self.center.z + self.w/2) - origin.z) / direction.z

            if tzmin > tzmax:
                tzmin, tzmax = tzmax, tzmin
            
            if tmin > tzmax or tzmin > tmax:
                return False
            
            if tzmin > tmin:
                tmin = tzmin
            
            if tzmax < tmax:
                tmax = tzmax

            normal = V3(0, 0, 0)
            impact = origin + (direction * tmin)

            impact = V3(round(impact.x, 3), round(impact.y, 3), round(impact.z, 3))

            if impact.x >= min.x and impact.y >= min.y and impact.z == min.z:
                normal = V3(0, 0, -1)
                porcent = ((impact.x - min.x) / self.w, (impact.y - min.y) / self.w)
            
            elif impact.x >= min.x and impact.y >= min.y and impact.z == max.z:
                normal = V3(0, 0, 1)
                porcent = ((impact.x - min.x) / self.w, (impact.y - min.y) / self.w)

            elif impact.x >= min.x and impact.y == min.y and impact.z >= min.z:
                normal = V3(0, -1, 0)
                porcent = ((impact.x - min.x) / self.w, (impact.z - min.z) / self.w)

            elif impact.x >= min.x and impact.y == max.y and impact.z >= min.z:
                normal = V3(0, 1, 0)
                porcent = ((impact.x - min.x) / self.w, (impact.z - min.z) / self.w)
            
            elif impact.x == min.x and impact.y >= min.y and impact.z >= min.z:
                normal = V3(-1, 0, 0)
                porcent = ((impact.z - min.z) / self.w, (impact.y - min.y) / self.w)
            
            elif impact.x == max.x and impact.y >= min.y and impact.z >= min.z:
                normal = V3(1, 0, 0)
                porcent = ((impact.z - min.z) / self.w, (impact.y - min.y) / self.w)

            if normal == V3(0, 0, 0):
                return False

            if tmin < 0:
                return False

            return Intersect(
                distance = tmin,
                point = impact,
                normal = normal,
                porcentaje = porcent
            )