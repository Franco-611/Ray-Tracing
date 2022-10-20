class Material:
    def __init__(self, diffuse, albedo, spec, refraction=0, texture=None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refraction = refraction
        if texture:
            self.textura = texture
        else:
            self.textura = None
        