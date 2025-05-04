Encapsulation is one of the major concept in object oriented programming. It helps to wrap up data and methods into a single unit. Through encapsulation, we can achieve the security and prevent the accidental modification of any attributes in a class

## **Access Modifiers**
Below are the three different types of access modifiers available in python

    1. Public Members
    2. Private Members
    3. Protected Members

| Access Modifiers | Own class access | Derived class access | object access
| :------------ |-----: |-----: |-----: |
| **private member** | YES | NO | NO |
| **protected member** | YES | YES | NO |
| **public member** | YES | YES | YES |

## **Public Members**
Public members can be accessed from anywhere in the program

    #ENCAPSULATION
    class Department:
        department = "CS"
            
    class Student(Department):
        def __init__(self, name, age):
            self.name = name
            self.age = 18
        
        def get_student_age(self):
            return "Age of the student is : {}".format(self.age)
            
        def get_department_name(self):
            return "Department of the student is : {}".format(self.department)
            
    student = Student("John", 18)
    #Public members can access from anywhere
    print("Name of the student is : {}".format(student.name))
    print(student.get_student_age())
    print(student.get_department_name())

 Output

    Name of the student is : John
    Age of the student is : 18
    Department of the student is : CS

## **Protected Members**
Protected members cannot be accessed in the child class like the below example

    #ENCAPSULATION
    class Department:
        _department = "CS"
            
    class Student(Department):
        def __init__(self, name, age):
            self.name = name
            self.age = 18
        
        def get_student_age(self):
            return "Age of the student is : {}".format(self.age)
        
        #Child accessing parent protected member- raises exception 
        def get_department_name(self):
            return "Department of the student is : {}".format(self.department)
            
    student = Student("John", 18)
    print("Name of the student is : {}".format(student.name))
    print(student.get_student_age())
    print(student.get_department_name())

 Output

    Name of the student is : John
    Age of the student is : 18
    Traceback (most recent call last):
    File "<string>", line 21, in <module>
    File "<string>", line 15, in get_department_name
    AttributeError: 'Student' object has no attribute 'department'

## **Private Members**
Private members cannot be accessed in the child class and its own objects too

    #ENCAPSULATION
    class Department:
        department = "CS"
            
    class Student(Department):
        def __init__(self, name, age):
            self.__name = name
            self.__age = 18
        
        def get_student_age(self):
            return "Age of the student is : {}".format(self.__age)
        
        #Child accessing parent protected member- raises exception 
        def get_department_name(self):
            return "Department of the student is : {}".format(self.department)
            
    student = Student("John", 18)
    print(student.get_student_age())
    #Raises Exception - Private members cannot access via object
    print("Name of the student is : {}".format(student.__name))
    print(student.get_department_name())

 Output

    Age of the student is : 18
    Traceback (most recent call last):
    File "<string>", line 20, in <module>
    AttributeError: 'Student' object has no attribute '__name'