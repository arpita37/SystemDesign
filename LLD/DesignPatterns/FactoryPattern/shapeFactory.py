from DesignPatterns.FactoryPattern.diffShapes.shapeCircle import ShapeOfCircle
from DesignPatterns.FactoryPattern.diffShapes.shapeRectangle import ShapeOfRectangle
from DesignPatterns.FactoryPattern.diffShapes.shapeSquare import ShapeOfSquare


class ShapeFactory:
    def __init__(self, shape : str):
        shape = shape.upper()
        print(shape)
        match shape:
            case "CIRCLE":
                self.obj = ShapeOfCircle()
            case "RECTANGLE":
                self.obj = ShapeOfRectangle()
            case "SQUARE":
                self.obj = ShapeOfSquare()
            case _:
                self.obj = None


    def draw(self):
        self.obj.draw()