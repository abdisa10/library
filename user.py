class User:
    def __init__(self,name,card_number):
        self.name = name
        self.card_number = card_number
    
    def return_list(self):
        user_list = []
        user_list.append(self.name)
        user_list.append(self.card_number)
        return user_list

