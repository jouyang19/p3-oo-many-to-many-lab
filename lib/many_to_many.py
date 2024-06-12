class Author:
    
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    def contracts(self):
        author_contracts = []
        for contract in Contract.all:
            if contract.author is self:
                author_contracts.append(contract)
        return author_contracts
    
    def books(self):
        author_books = []
        for contract in self.contracts():
            author_books.append(contract.book)
        return author_books
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Book:
    def __init__(self, title):
        self.title = title
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
        
    def contracts(self):
        book_contracts = []
        for contract in Contract.all:
            if contract.book is self:
                book_contracts.append(contract)
        return book_contracts
    
    def authors(self):
        book_authors = []
        for contract in self.contracts():
            book_authors.append(contract.author)
        return book_authors

class Contract:
    all = []
    
    @classmethod
    def contracts_by_date(self, date):
        contracts_list = []
        for contract in Contract.all:
            if contract.date == date:
                contracts_list.append(contract)
        return contracts_list
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception('Author should be an author object')
    
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception('Book should be a Book object')
        
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = new_date
        else:
            raise Exception('date should be a string')
    
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, new_royalties):
        if isinstance(new_royalties, int):
            self._royalties = new_royalties
        else:
            raise Exception('royalties should be an integer')
    