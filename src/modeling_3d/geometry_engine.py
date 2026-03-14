# 3D Geometry Modeling Engine

class GeometryEngine:
    def __init__(self):
        # Initialize the geometry engine
        self.geometries = []

    def add_geometry(self, geometry):
        """Add a new geometry to the engine."""
        self.geometries.append(geometry)

    def remove_geometry(self, geometry):
        """Remove a geometry from the engine."""
        self.geometries.remove(geometry)

    def render(self):
        """Render all geometries."""
        for geometry in self.geometries:
            geometry.draw()  # Assuming each geometry has a draw method

# Example Geometry class
class Geometry:
    def __init__(self, name):
        self.name = name
    
    def draw(self):
        print(f"Drawing {self.name}")  

# Usage
if __name__ == '__main__':
    engine = GeometryEngine()
    cube = Geometry("Cube")
    sphere = Geometry("Sphere")
    engine.add_geometry(cube)
    engine.add_geometry(sphere)
    engine.render()