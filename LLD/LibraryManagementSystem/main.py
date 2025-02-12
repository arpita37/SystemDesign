import time

from model.book import Book
from model.member import Member
from publicInterfaces.libraryManager import LibraryManager


class Demo:
    @staticmethod
    def run():
        obj = LibraryManager()
        obj.getInstance()
        b1 = Book(1,"Book1","abcd","2020",2)
        b2 = Book(2, "Book2", "bcde", "2021", 1)
        b3 = Book(3, "Book3", "efgh", "2010", 3)
        b4 = Book(4, "Book4", "ijkl", "2000", 1)
        obj.add_book(b1)
        obj.add_book(b2)
        obj.add_book(b3)
        obj.add_book(b4)
        user1 = Member("arpita",1,"abasak@gmail.com")
        user2 = Member("Kingshuk", 2, "kbose@yahoo.com")
        obj.addMember(user1)
        obj.addMember(user2)
        time.sleep(1)
        obj.showBooks()
        time.sleep(1)
        obj.borrowBook(1,2)
        user1.getBooks()
        time.sleep(1)
        obj.borrowBook(1,2)
        time.sleep(1)
        obj.borrowBook(2,2)


if __name__ == "__main__":
    Demo.run()