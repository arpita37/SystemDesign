import datetime
import time

from Models.contactTypes import ContactType
from Models.guest import Guest
from Models.room import Room
from Models.roomTypes import Roomtype
from PublicInterfaces.hotelmanagementsystem import HotelManageMentsystem


class Demo:
    @staticmethod
    def run():
        obj = HotelManageMentsystem()
        obj.getInstance()
        r1 = Room(101,1,Roomtype.SINGLE)
        r2 = Room(102, 1, Roomtype.DOUBLE)
        r3 = Room(201, 2, Roomtype.DELUXE)
        r4 = Room(202, 2, Roomtype.SINGLE)
        r5 = Room(301, 3, Roomtype.SUITE)
        r6 = Room(302, 3, Roomtype.SINGLE)
        arr = [r1,r2,r3,r4,r5,r6]
        for item in arr:
            obj.addRoom(item)

        obj.showRooms()
        time.sleep(0.01)
        obj.checkAvailability(101,datetime.datetime.today(), datetime.datetime.today()+datetime.timedelta(days=4))
        time.sleep(1)
        g1 = Guest(1234, "Arpita", ContactType.MAIL, "arpitabasak031286@gmail.com")
        obj.bookroom(101,datetime.datetime.today(), datetime.datetime.today()+datetime.timedelta(days=4), g1)
        time.sleep(3)
        obj.checkin(101,g1)
        time.sleep(2)
        obj.checkout(101, g1)

if __name__ == "__main__":
    Demo.run()
