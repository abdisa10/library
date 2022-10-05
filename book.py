class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year  
    
    def return_list(self):
        book_list = []
        book_list.append(self.title)
        book_list.append(self.author)
        book_list.append(self.year)
        return book_list

