class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(f"First Name: {self.first}\nLast Name: {self.last}\nEmail: {self.email}\nAge: {self.age}\nMember: {self.is_rewards_member}\nCurrent Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("You already have a membership!")
        else:
            self.gold_card_points += 200
            self.is_rewards_member = True
        return self
    
    def spend_points(self,amount):
        if self.gold_card_points - amount <= 0:
            print("Not Enough Points")
        else:
            self.gold_card_points -= amount
        return self

user1 = User("Joe", "Smith", "joesmith@comcast.net", "22")
user1.display_info().enroll().display_info().spend_points(50).display_info()

user2 = User("Ryan", "Kochen", "rkochen@comcast.net", "20")
user2.display_info().enroll().display_info().spend_points(80).display_info()
