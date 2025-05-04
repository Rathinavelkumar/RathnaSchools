Normally, we can pass the arguments to function either by position and Keyword. But we can also restrict the user with optional (/ and *) symbols which decides how the argument should be passed to function


## **Function Definition**

As per python documentation, please find below the function definition

    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        -----------    ----------     ----------
            |             |                  |
            |        Positional or keyword   |
            |                                - Keyword only
            -- Positional only

## **Types of Special Parameters**

* `positional-only`

* `positional-or-keyword`

* `keyword-only`

## **Positional Only**
Below function indicates that it must call with first two parameters are positional and last two parameter are either keyword or positional

    #Positional Only
    def sum(num1, num2, /, num3, num4):
        result = num1 + num2 + num3 + num4
        print(result)
        
    #Four positional
    sum(10, 20, 30, 40)

    #Three Positional and One Keyword
    sum(10, 20, 30, num4=40)

    #Two Positional and Two Keyword
    sum(10, 20, num3=30, num4=40)

 Output

    100
    100
    100

If we call function with more than two keywords arguments raises exception

    #Positional Only
    def sum(num1, num2, /, num3, num4):
        result = num1 + num2 + num3 + num4
        print(result)
        
    #One Positional and Three Keyword - Raises Exception
    sum(10, num2=20, num3=30, num4=40)

 Output

    Traceback (most recent call last):
    File "<string>", line 7, in <module>
    TypeError: sum() got some positional-only arguments passed as keyword arguments: 'num2'

## **Positional or Keyword**
Below function indicates we can pass all arguments either positional-or-keyword 

    #Positional or Keyword
    def sum(num1, num2,  num3, num4):
        result = num1 + num2 + num3 + num4
        print(result)

    #Four positional
    sum(10, 20, 30, 40)

    #Three Positional and One Keyword
    sum(10, 20, 30, num4=40)

    #Two Positional and Two Keyword
    sum(10, 20, num3=30, num4=40)

    #One Positional and Three Keyword
    sum(10, num2=20, num3=30, num4=40)

    #Four Keyword
    sum(num1=10, num2=20, num3=30, num4=40)

 Output

    100
    100
    100
    100
    100

## **Keyword Only**
Below function indicates that it must call with first two arguments as positional and last two arguments as keyword

    #Positional or Keyword
    def sum(num1, num2, *, num3, num4):
        result = num1 + num2 + num3 + num4
        print(result)

    #Two Positional and Two Keyword
    sum(10, 20, num3=30, num4=40)

    #One Positional and Three Keyword
    sum(10, num2=20, num3=30, num4=40)

    #Four Keyword
    sum(num1=10, num2=20, num3=30, num4=40)

 Output

    100
    100
    100

If we call function with more than two positional arguments raises exception

    #Positional Only
    def sum(num1, num2, /, num3, num4):
        result = num1 + num2 + num3 + num4
        print(result)

    #Four positional
    sum(10, 20, 30, 40)

    #Three Positional and One Keyword
    sum(10, 20, 30, num4=40)

    #Two Positional and Two Keyword
    sum(10, 20, num3=30, num4=40)

 Output

    Traceback (most recent call last):
    File "<string>", line 7, in <module>
    TypeError: sum() takes 2 positional arguments but 4 were given

