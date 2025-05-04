Iterators helps to iterate the iterable objects like list, tuple, set and dict in python. We can create custom iterator for the python functions

## **Iterators**
Two function  - **iter** and **next** helps to achieve the iterate over the given data in python like the below example

    num_list = [10, 20, 30, 40, 50]

    #Make the num list iterable
    iter_num_list = iter(num_list)

    while num_list:
        try:
            print(next(iter_num_list))
        #No more elements raises stop iteration exception
        except StopIteration:
            break

 Output

    10
    20
    30
    40
    50

## **Custom Iterators**
Implementation of custom iterators for our function is very easier. With the help of `__iter__` and `__next__` methods, we can build the custom iterators like the below example

    #Custom Iterator 
    class TenMultipler:
        def __init__(self, multiple, max_limit):
            self.multiple = multiple
            self.max_limit = max_limit
            
        def __iter__(self):
            self.start = self.multiple
            return self
        
        def __next__(self):
            result = self.multiple * 10
            if result <= self.max_limit:
                self.multiple = self.start + self.multiple
                return result
            else:
                raise StopIteration
                
    tenMultipler = TenMultipler(2, 100)
    iter_tenMultipler = iter(tenMultipler)
    while iter_tenMultipler:
        try:
            print(next(iter_tenMultipler))
        except:
            print("Max limit reached - Iteration stopped")
            break

 Output

    20
    40
    60
    80
    100
    Max limit reached - Iteration stopped