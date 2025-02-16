import datetime
import time

from models.menuItem import Menuitem
from models.reservation import Reservation
from models.staff import Staff
from publicInterfaces.restaurantManagement import RestaurantManagement


class Demo:
    @staticmethod
    def run():
        obj = RestaurantManagement()
        obj.get_instance()

        #menu operations
        m1 = Menuitem(1,"Chicken Biriyani","Chieckn Biriyani",300,True)
        m2 = Menuitem(2, "Mutton Biriyani", "Mutton Biriyani", 500, True)
        m3 = Menuitem(3, "Veg Biriyani", "Veg Biriyani", 200, True)
        m4 = Menuitem(4, "Paneer Biriyani", "Paneer Biriyani", 250, True)
        m5 = Menuitem(5, "Mushroon Biriyani", "Mushroom Biriyani", 250, True)
        m6 = Menuitem(6, "Aloo Biriyani", "Aloo Biriyani", 150, True)

        menus = [m1,m2,m3,m4,m5,m6]
        for m in menus:
            obj.addMenu(m)
        time.sleep(1)
        obj.showMenu()
        time.sleep(1)

        #staff opetaions
        st1 = Staff(1,"Kingshuk","Server","kbose@gmail.com")
        st2 = Staff(2,"Adi","Manager","akar@gmail.com")
        obj.addStaff(st1)
        obj.addStaff(st2)

        #reservation operations
        id = obj.addReservation("Arpita","801762733",10,datetime.datetime.today()+datetime.timedelta(days=6))

        #order
        obj.order()

if __name__ == "__main__":
    Demo.run()
