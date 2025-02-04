from datetime import datetime
from Models.car import Car
from Models.user import User
from PublicInterfaces.rentalSystem import RentalSystem


class Demo:
    @staticmethod
    def run():
        obj = RentalSystem()
        obj.get_instance()

        car1 = Car(1,"Fiat", "Classy", "suv", "2022", 1000)
        car2 = Car(2,"Swift", "Maruti", "normal", "2018", 400)
        car3 = Car(3,"Baleno", "Nexus", "xuv", "2020", 800)

        obj.add_cars(car1)
        obj.add_cars(car2)
        obj.add_cars(car3)

        obj.browseCars()
        user1 = User("Arpita", "87198698261", "ABC-Arpita")
        user2 = User("Kingshuk", "87198698261", "ABC-Kingshuk")

        obj.addUser(user1)
        obj.addUser(user2)
        ct = obj.reserveCar(user1,1,"2025-02-10","2025-02-12")
        user1.contract = ct
        obj.reserveCar(user2,1,"2025-02-10","2025-02-12")

        #obj.cancelReservation(1,ct)
        obj.returnCar(1,ct)


if __name__ == "__main__":
    Demo.run()