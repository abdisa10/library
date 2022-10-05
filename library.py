import random
from user import User
from book import Book



class Library:
    def __init__(self):
        self.bookList = []
        self.userList = []
        self.checkedoutbooks = []
        self.checkouts = {}
        
    def add_book(self,title,author,year):
        book = Book(title,author,year)
        self.bookList.append(book.return_list())
        
    def remove_book(self,title):
        for book in range(len(self.bookList)):
            if title == self.bookList[book][0]:
                del self.bookList[book]


    
    def checkout_book(self,card_number,title):
        if  bool(self.checkouts):
            
            if '{}'.format(card_number) in self.checkouts:
                self.checkedoutbooks = self.checkouts['{}'.format(card_number)]
                for i in range(len(self.userList)):
                    if self.userList[i][1] == card_number:
                        for book in range(len(self.bookList)):
                            if title == self.bookList[book][0]:
                                self.checkedoutbooks.append(self.bookList[book])
                                self.checkouts['{}'.format(card_number)] = self.checkedoutbooks
                    
            else:
                self.checkedoutbooks = []
                for i in range(len(userList)):
                    if self.userList[i][1] == card_number:
                        for book in range(len(self.bookList)):
                            if title == self.bookList[book][0]:
                                self.checkedoutbooks.append(self.bookList[book])
                                self.checkouts['{}'.format(card_number)] = self.checkedoutbooks
                      
        else:
            for book in range(len(self.bookList)):
                        if title == self.bookList[book][0]:
                            self.checkedoutbooks.append(self.bookList[book])
                            self.checkouts['{}'.format(card_number)] = self.checkedoutbooks

        


                
    def return_book(self,card_number,title):
        if '{}'.format(card_number) in self.checkouts:
            self.checkedoutbooks = self.checkouts['{}'.format(card_number)]
            for i in range(len(self.userList)):
                if self.userList[i][1] == card_number:
                    for book in range(len(self.bookList)):
                        if title == self.bookList[book][0]:
                            del self.checkedoutbooks[self.checkedoutbooks.index(self.bookList[book])]
                            self.checkouts['{}'.format(card_number)] = '{}'.format(self.checkedoutbooks)
        else:
                return str('No books to return')
            
            
        

    
    def add_user(self,name):
        count = 0
        if self.userList == []:
            user = User(name,count)
            self.userList.append(user.return_list())
            print('Your card number is {}.'.format(count))
        else:
            for user in range(len(self.userList)):
                while count == self.userList[user][1]:
                    count += 1
            user = User(name,count)
            self.userList.append(user.return_list())
            print('Your card number is {}.'.format(count))
        
    def remove_user(self,card_number):
        for user in range(len(self.userList)):
            if card_number == self.userList[i][1]:
                del self.userList[i]



