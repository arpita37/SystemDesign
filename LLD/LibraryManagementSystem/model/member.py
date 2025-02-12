from collections import defaultdict
from typing import List


class Member:
    def __init__(self,name,id,contact):
        self.name = name
        self.id = id
        self.contact = contact
        self.books = defaultdict(list) #dict of book Ids

    def getName(self): return self.name
    def getId(self): return self.id
    def getContact(self): return self.contact
    def getBooks(self):
        print(f"\nBOOK_ID\tNAME\tAUTHOR")
        for key,val in self.books.items():
            print(f"\n{val[0].getId()}\t{val[0].getName()}\t{val[0].getAuthor()}")

    def checkIfBorrowed(self,bookId):
        if bookId in self.books:
            return True
        return False
    def checkNoOfBooks(self):
        return len(self.books)
    def addBook(self,book,date):
        self.books[book.getId()] = (book,date)

    def removeBook(self,bookId):
        self.books.pop(bookId)
    def getBook(self,isbn):
        return self.books[isbn]
