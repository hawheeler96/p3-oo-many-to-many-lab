class Author:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        royalties_sum = 0
        author_royalties = [contract.royalties for contract in Contract.all if contract.author is self]
        for royalties in author_royalties:
            royalties_sum += royalties
        return royalties_sum
            
            

class Book:
    
    all = []
    
    def __init__(self, title):
        self.title = title
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]


class Contract:
    
    all = []
    
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
            self.date = date
            self.royalties = royalties
            self.author = author
            self.book = book
            Contract.all.append(self)
        else: 
            raise Exception("dumbass")
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date is date]
