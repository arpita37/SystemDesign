from DesignPatterns.FactoryPattern.diffShapes.shapeCircle import ShapeOfCircle
from DesignPatterns.FactoryPattern.shapeFactory import ShapeFactory


def main():
    circleObj = ShapeFactory("Circle")
    rectObj = ShapeFactory("REctangle")
    squareObj = ShapeFactory("sqUare")

    circleObj.draw()
    rectObj.draw()
    squareObj.draw()


if __name__ == "__main__":
    main()