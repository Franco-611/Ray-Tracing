from material import *
from color import *

rubber = Material(diffuse=color(80, 0, 0), albedo=[0.9, 0.1,0,0], spec=10)
ivory = Material(diffuse=color(100, 100, 80), albedo=[0.6, 0.3,0,0], spec=50)
mirror = Material(diffuse=color(255,255, 255), albedo=[0, 1, 0.8,0], spec=1425)
glass = Material(diffuse=color(150,180, 200), albedo=[0, 0.5, 0.1, 0.8], spec=125, refraction=1.5)