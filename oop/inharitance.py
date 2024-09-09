from class_object import User 

# Inharitance:
class Customer(User):

    # Constructor
    def __init__(self,name,age):
        # Call the parent class constructor using super()
        super().__init__(name, age) 
        
        self.balance=0
    
    def set_balance(self,balance):
        self.balance=balance
        
    # Override
    def gretting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    
sobuj=Customer('Sobuj',27)
sobuj.set_balance(3000)
# sobuj.has_birthday() # Here can access parent class method.
print(sobuj.gretting())