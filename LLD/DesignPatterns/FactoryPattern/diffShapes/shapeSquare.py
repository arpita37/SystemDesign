from DesignPatterns.FactoryPattern.diffShapes.diffShapesInterface import DiffShapes


class ShapeOfSquare(DiffShapes):
    def __init__(self):
        super().__init__()

    def draw(self):
        print("This is the shape of square")