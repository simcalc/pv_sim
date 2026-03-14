# piping_component.py

class PipingComponent:
    def __init__(self, name, diameter, material):
        self.name = name
        self.diameter = diameter
        self.material = material

    def __str__(self):
        return f'PipingComponent(name={self.name}, diameter={self.diameter}, material={self.material})'


class Valve(PipingComponent):
    def __init__(self, name, diameter, material, type):
        super().__init__(name, diameter, material)
        self.type = type

    def __str__(self):
        return f'Valve(name={self.name}, diameter={self.diameter}, material={self.material}, type={self.type})'


class Pipe(PipingComponent):
    def __init__(self, name, diameter, material, length):
        super().__init__(name, diameter, material)
        self.length = length

    def __str__(self):
        return f'Pipe(name={self.name}, diameter={self.diameter}, material={self.material}, length={self.length})'