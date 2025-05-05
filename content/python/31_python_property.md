Property is one of the most important concepts in python. Its performs the same operation of getter and setter in other programing languages

## Normal function
Below program is a simple one which is not validating the age of the voter and allow them to add in voter list

    class Voters:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def add_to_voter_list(self):
            print("Name: {} | Age: {} - Added to voters list successfully".format(self.name, self.age))
        
    voter = Voters("John", 22)
    voter.add_to_voter_list()

 Output

    Name: John | Age: 22 - Added to voters list successfully


## Get and Set function
To overcome the problem in above program, we have implemented the get and set age functions and also validating the age is greater than 18

    class Voters:
        def __init__(self, name, age):
            self.name = name
            self.set_age(age)
        
        def add_to_voter_list(self):
            print("Name: {} | Age: {} - Added to voters list successfully".format(self.name, self.age))
            
        #Getting the age
        def get_age(self):
            return self.age
        
        #Setting the age
        def set_age(self, age):
            if age>18:
                self.age = age
            else:
                raise ValueError("Age should be greater than 18")
        
    voter1 = Voters("John", 28)
    voter1.add_to_voter_list()

    voter2 = Voters("David", 15)
    voter2.add_to_voter_list()

 Output

    Name: John | Age: 28 - Added to voters list successfully
    Traceback (most recent call last):
    File "<string>", line 21, in <module>
    File "<string>", line 4, in __init__
    File "<string>", line 16, in set_age
    ValueError: Age should be greater than 18

## Issue in get and set method without property
But this program also have another issue, it is not allowing voter object to access its age attribute

    class Voters:
        def __init__(self, name, age):
            self.name = name
            self.set_age(age)
        
        def add_to_voter_list(self):
            print("Name: {} | Age: {} - Added to voters list successfully".format(self.name, self._age))
            
        #Getting the age
        def get_age(self):
            return self._age
        
        #Setting the age
        def set_age(self, age):
            if age>18:
                self._age = age
            else:
                raise ValueError("Age should be greater than 18")
        
    voter1 = Voters("John", 28)
    voter1.add_to_voter_list()
    print(voter1.name)
    #It raises the error
    print(voter1.age)

 Output

    Name: John | Age: 28 - Added to voters list successfully
    John
    Traceback (most recent call last):
    File "<string>", line 23, in <module>
    AttributeError: 'Voters' object has no attribute 'age'


## Property class implementation
With the help of property class declaration for age, we can overcome the above issue and also validate the age value in our code like the below example program

    class Voters:
        def __init__(self, name, age):
            self.name = name
            self.set_age(age)
        
        def add_to_voter_list(self):
            print("Name: {} | Age: {} - Added to voters list successfully".format(self.name, self._age))
            
        #Getting the age
        def get_age(self):
            return self._age
        
        #Setting the age
        def set_age(self, age):
            if age>18:
                self._age = age
            else:
                raise ValueError("Age should be greater than 18")
        
        #property declaration resolves the issue
        age = property(get_age, set_age)
        
    voter1 = Voters("John", 28)
    voter1.add_to_voter_list()
    print(voter1.name)
    print(voter1.age)

 Output

    Name: John | Age: 28 - Added to voters list successfully
    John
    28

## Property Annotation
The same functionality can be achieved with the help of property annotations like the below example. Its pythonic way of implementing getter and setter functionality in our programs

class Voters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def add_to_voter_list(self):
        print("Name: {} | Age: {} - Added to voters list successfully".format(self.name, self.age))
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value>18:
            self._age = value
        else:
            raise ValueError("Age should be greater than 18")
        
    voter1 = Voters("John", 22)
    voter1.add_to_voter_list()
    print(voter1.name)
    print(voter1.age)

 Output

    Name: John | Age: 22 - Added to voters list successfully
    John
    22