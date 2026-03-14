class PressureVessel:
    def __init__(self, diameter, height, material):
        self.diameter = diameter
        self.height = height
        self.material = material

    def calculate_volume(self):
        import math
        radius = self.diameter / 2
        return math.pi * (radius ** 2) * self.height

    def get_material(self):
        return self.material


class Cylinder(PressureVessel):
    def __init__(self, diameter, height, material):
        super().__init__(diameter, height, material)

    def calculate_surface_area(self):
        import math
        radius = self.diameter / 2
        return 2 * math.pi * radius * (radius + self.height)


class Sphere(PressureVessel):
    def __init__(self, diameter, material):
        super().__init__(diameter, diameter, material)

    def calculate_volume(self):
        radius = self.diameter / 2
        return (4/3) * math.pi * (radius ** 3)