class User:
    # Constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age 

    def gretting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age+=1
        return self.gretting()

# Only run this code if this file is executed directly
if __name__ == '__main__':
    # Object
    shaiful = User('Shaiful Islam', 24)
    print(shaiful.name)
    print(shaiful.has_birthday())

