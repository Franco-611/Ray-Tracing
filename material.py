class Material:
    def __init__(self, diffuse, albedo, spec, refraction=0):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refraction = refraction