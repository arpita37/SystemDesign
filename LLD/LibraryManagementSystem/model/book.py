class Book:
    def __init__(self,id,title,author,publication_year,copies):
        self.id = id
        self.title = title
        self.author = author
        self.year = publication_year
        self.copies = copies

    def getId(self): return self.id
    def getName(self): return self.title
    def getAuthor(self): return self.author
    def getYear(self): return self.year
    def getCopies(self): return self.copies
    def addCopy(self,item): self.copies += item
    def removeCopy(self,item): self.copies -= item