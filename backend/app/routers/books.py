from typing import Optional


class Book:   
            
    #private variable to get unique id for books 
    # - need figure it out concurrency issue later
    _id_counter = 0    
    
    book_id: int
    title: str
    author: Optional[str] = None
    isbn: Optional[int] = None
    status: Optional[str] = None
    
    
    def __init__(self, title) -> None:
        self.title = title
        self.book_id = Book._get_next_id()

    
     
     
     
     
     
     
    ###################################################################################    
    #private function to get unique id for books 
    # - need figure it out concurrency issue later
    @classmethod
    def _get_next_id(cls):
        cls._id_counter += 1
        return cls._id_counter
        
    #helpper function
    #getters
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    def get_isbn(self):
        return self.isbn
        
    def get_status(self):
        return self.status 
    
    def get_book_id(self):
        return self.book_id
    
    #setters
    def set_title(self, title):
        self.title = title
    
    def set_author(self, author):
        self.author = author
        
    def set_isbn(self, isbn):
        self.isbn = isbn
        
    def set_status(self, status):
        self.status = status
    
    
    
###############################################################
#test
###############################################################

b1 = Book("New Book")
b2 = Book("New Book2")


print(b1.get_title())
print(b1.get_book_id())

print(b2.get_title())
print(b2.get_book_id())