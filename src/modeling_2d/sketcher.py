# 2D Sketching and Drawing Module

class Sketcher:
    def __init__(self):
        self.shapes = []

    def draw_circle(self, x, y, radius):
        circle = {'type': 'circle', 'x': x, 'y': y, 'radius': radius}
        self.shapes.append(circle)
        return circle

    def draw_rectangle(self, x, y, width, height):
        rectangle = {'type': 'rectangle', 'x': x, 'y': y, 'width': width, 'height': height}
        self.shapes.append(rectangle)
        return rectangle

    def clear_sketch(self):
        self.shapes.clear()  

    def get_sketch(self):
        return self.shapes

# Example Usage:
# sketcher = Sketcher()
# sketcher.draw_circle(5, 5, 10)
# sketcher.draw_rectangle(2, 3, 4, 5)
# print(sketcher.get_sketch())