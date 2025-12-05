class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # Return all Contract instances related to this book
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        # Return all authors that have contracts for this book
        return [c.author for c in self.contracts()]

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return all Contract instances related to this author
        return [c for c in Contract.all if c.author == self]

    def books(self):
        # Return all books associated with this author via contracts
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]
