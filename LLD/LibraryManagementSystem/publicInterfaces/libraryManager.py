import logging
from threading import Lock
from datetime import datetime
from model.book import Book

logging.basicConfig(level=logging.INFO)
class LibraryManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.catalog = dict()
            cls._instance.members = dict()
            cls._instance.MAX_BOOKS_PER_MEMBER = 5
            cls._instance.MAX_ALLOTED_DAYS = 15
            cls._instance.lock =Lock()
            cls._instance.log = logging.getLogger("LibraryManagement")
        return cls._instance

    def getInstance(cls):
        if not cls._instance:
            LibraryManager()
        return cls._instance

    def add_book(self, book: Book):
        id = book.getId()
        if id not in self.catalog:
            self.catalog[book.getId()] = book
        else:
            obj = self.catalog[book.getId()]
            obj.addCopy(1)

    def remove_book(self, isbn: str):
        if isbn in self.catalog:
            self.catalog.pop(isbn, None)

    def get_book(self, isbn: str):
        if isbn not in self.catalog:
            self.log.info(f"\nBook {isbn} does not exist")
            return None
        return self.catalog.get(isbn)

    def showBooks(self):
        print(f"\nBOOK_ID\tNAME\tAUTHOR")
        for key,val in self.catalog.items():
            print(f"\n{key}\t{val.getName()}\t{val.getAuthor()}")

    def addMember(self,mem):
        id = mem.getId()
        if id not in self.members:
            self.members[id] = mem
            self.log.info(f"\nMember {id} added succesfully!!")
        else:
            self.log.warning(f"\nMemebr {id} already exists")

    def removeMember(self,mem):
        id = mem.getId()
        if id not in self.members:
            self.log.info(f"\nMember {id} does not exist!!")
        else:
            booksBorrowd = mem.checkNoOfBooks()
            if booksBorrowd != 0:
                self.log.warning(f"\nCan't rmeove member {id} as he/she has borrowed books!!")
                return
            self.members.pop(id)
            self.log.info(f"\nMemebr {id} has been removed!!")

    def getMember(self,memId):
        if memId not in self.members:
            self.log.info(f"\nMember {memId} does not exist")
            return None
        return self.members[memId]

    def searchBookByName(self,keyword):
        matchingBooks = []
        for key,val in self.catalog.items():
            if keyword in val.getName():
                matchingBooks.append(val.getName())
        self.log.info(f"\nMatching books iwth keyword {keyword} are:")
        for val in matchingBooks:
            self.log.info(f"\n{val}")

    def borrowBook(self,userId,isbn):
        with self.lock:
            member = self.getMember(userId)
            try:
                noOfBorrowsBooks = member.checkNoOfBooks()
                if noOfBorrowsBooks == self.MAX_BOOKS_PER_MEMBER:
                    self.log.info(f"\nCan't borrow any more book!!!")
                    return
                book = self.get_book(isbn)
                if not book or book.getCopies() == 0:
                    self.log.info(f"\nBook {isbn} is not in available!!")
                    return
                if member.checkIfBorrowed(isbn):
                    self.log.warning(f"\nBook already borrowed by memeber!!!")
                    return
                book.removeCopy(1)
                member.addBook(book,datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
                self.log.info(f"\nBook {isbn} borrowed by {member.getName()}")
            except Exception as e:
                raise ValueError("User doesn't exist")

    def returnBook(self,userID,isbn):
        self.lock.acquire()
        member = self.getMember(userID)
        try:
            book,borrowedDate = member.getBook(isbn)
            delta = datetime.today().strftime("%Y-%m-%d %H:%M:%S")-borrowedDate
            if delta.days > self.MAX_ALLOTED_DAYS:
                self.log.info(f"Please pay Rs.{delta.days*5} as fine for {delta.days} days!!")
                #process Payment
                self.log.info(f"Payment successful!!")
            member.removeBook(isbn)
            self.catalog[isbn].addCopy(1)
            self.log.info(f"\nReturned book {isbn} by {member.getName()}")
        except Exception as e:
            raise ValueError("User doesn't exist")
        self.lock.release()