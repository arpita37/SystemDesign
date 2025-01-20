from DesignPatterns.DecoratorPattern.BasePizaa.margharitaPizza import MargharitaPizza
from DesignPatterns.DecoratorPattern.BasePizaa.veggieDelight import VeggieDelightPizza
from DesignPatterns.DecoratorPattern.Toppings.cheeseToppins import CheeseToppins
from DesignPatterns.DecoratorPattern.Toppings.jalapenoToppins import JalapenoToppins
from DesignPatterns.DecoratorPattern.Toppings.mushroomToppins import MushroomToppins


def main():
    pizzaObj1 = MargharitaPizza()
    marghaWCheese1 = CheeseToppins(pizzaObj1)
    print(f"The Margharita pizza with cheese toppins cost {marghaWCheese1.displayCost()}")

    pizzaObj2 = VeggieDelightPizza()
    vegDelightWCheese1 = MushroomToppins(pizzaObj2)
    print(f"The Veggie delight pizza with mushroom toppins cost {vegDelightWCheese1.displayCost()}")

if __name__ == "__main__":
    main()