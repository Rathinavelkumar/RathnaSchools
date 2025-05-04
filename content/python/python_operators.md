Operators are used to perform various mathematical operations on the data value. Operators are used to perform various mathematical operations on the data value

## **Types of Operators**

    1. Arithmetic operators 

    2. Comparison operators

    3. Logical operators

    4. Identity operators

    5. Membership operators 

    6. Bitwise operators

## **Arithmetic operators**
Arithmetic operators are used to perform simple arithmetic operations over the operands

    #Addition Operation
    add_result = 10 + 20
    print("Addition Result : {}".format(add_result))

    #Subtraction Operation
    sub_result = 100 - 50
    print("Subtraction Result : {}".format(sub_result))

    #Multiplication Operation
    multi_result = 10 * 20
    print("Multiplication Result : {}".format(multi_result))

    #Division Operation (Decimal Value)
    div_result = 25 / 10
    print("Division Result : {}".format(div_result))

    #Floor Division (Nearest Whole Number)
    floor_result = 25//10
    print("Floor Result : {}".format(floor_result))

    #Modulus Operation
    mod_result = 25%10
    print("Modulus Result : {}".format(mod_result))

    #Exponential Operation (2*2*2*2*2)
    exp_result = 2 ** 5
    print("Exponential Result : {}".format(exp_result))

 Output

    Addition Result : 30
    Subtraction Result : 50
    Multiplication Result : 200
    Division Result : 2.5
    Floor Result : 2
    Modulus Result : 5
    Exponential Result : 32

## **Comparison operators**
Comparison operators are used to check for relations between the operands

    #Equal Operator
    num1, num2 = 50, 50
    if num1==num2: print("Equal")

    #Not Equal Operator
    num1, num2 = 50, 100
    if num1!=num2: print("Not Equal")

    #Greater than Operator
    num1, num2 = 100, 50
    if num1>num2: print("Greater")

    #Greater than Operator
    num1, num2 = 50, 100
    if num1<num2: print("Lesser")

    #Greater than or Equal to
    num1, num2 = 50, 50
    if num1>=num2: print("Greater than or Equal to")

    #Lesser than or Equal to
    num1, num2 = 50, 50
    if num1<=num2: print("Lesser than or Equal to")

 Output

    Equal
    Not Equal
    Greater
    Lesser
    Greater than or Equal to
    Lesser than or Equal to

## **Logical operators**
Logical Operators are used to check conditional expression. We can use these operators in conditional and looping statement for evaluation

    #AND - Returns True If both conditions are True
    num = 50
    if num>10 and num<100: print(True)

    #OR - Returns True If any one of the conditions is True
    num = 50
    if num>10 or num<30: print(True)

    #NOT - Returns opposite of the result
    num = 50
    if not(num>100): print(True)

 Output

    True
    True
    True

## **Identity operators**
Identity operators are used to compare the object's memory location

== Operator usually compare the value of given objects

is operator compare the memory location of given objects. It returns True if both variables are the same object

    num_list1 = [1, 2, 3]
    num_list2 = [1, 2, 3]
    num_list3 = num_list1

    #Both have same data, So result is True
    print(num_list1 == num_list2)
    #Both have same data, So result is True
    print(num_list1 == num_list3)

    #Both are different object, So result is False
    print(num_list1 is num_list2)
    #Both are same object, So result is True
    print(num_list1 is num_list3)

 Output

    True
    True
    False
    True

## **Bitwise operators**
Bitwise operators are used to perform operations bit by bit

**Bitwise AND operator**

    num1 = 3
    num2 = 5

    #BITWISE AND Operator returns 1 if both the bits are 1
    print( num1&num2 )

 Output

    1

The result is 1, because 3 is equal to 0011 in binary and 5 is equal to 0101 in binary

Now compare each bit between 3 and 5, only last bit are 1 for both, so that alone returns 1 in final result. Hence, 0001 decimal value is 1, that is get printed in final output

    0011 = 3
    0101 = 5
    ----------
    0001 = 1

**Bitwise OR operator**

    num1 = 3
    num2 = 5

    #BITWISE OR Operator returns 1 if anyone of two bits are 1
    print( num1 | num2 )

 Output

    1


The result is 7, because 3 is equal to 0011 in binary and 5 is equal to 0101 in binary

Now compare each bit between 3 and 5, the last three having latest one of two bits is 1, so that three bits returns 1. Hence, 0111 decimal value is 7, that is get printed in final output

    0011 = 3
    0101 = 5
    ----------
    0111 = 7

**Bitwise XOR operator**

    num1 = 3
    num2 = 5

    #BITWISE XOR Operator returns 1 if both bit are not equal
    print( num1 ^ num2 )

 Output

    6

The result is 6, because 3 is equal to 0011 in binary and 5 is equal to 0101 in binary 

Now compare each bit between 3 and 5, only 2nd and 3rd third sets having one of the bit is 1 and other is 0, so that two bits returns 1. Hence, 0111 decimal value is 6, that is get printed in final output

    0011 = 3
    0101 = 5
    ----------
    0110 = 6


**Bitwise NOT operator**

    num = 3

    #BITWISE NOT Operator returns 1's compliment of the number
    print( ~num )

 Output

    -4

The result is -4, because 3 is equal to 0011 in binary First it add last bit 1+1 = 10 in binary (0 is result and 1 is carry)

Second it add second bit 1 with carry 1 which means 1+1 = 10 in binary (0 is result and 1 is carry) 

Third it add third bit 0 with carry 1 which means 1+0=0 in binary (no carry) Fourth it only have one bit 0 and no carry, so result in 0

Since its a 1's compliment we should have - value for the output decimal, so it gives -0100 as -4 in decimal output.

    0011 = 3
    -      1
    --------------
    - 0100 = -4


**Left shift operator**

    num = 3

    #LEFT SHIFT - Shifting Bit to Leftmost
    print( num<<2 )

 Output

    12

The result is 12, since the bits are pushing from left to right (2 places movement since we gave <<2 )

    0011 = 3
    <<2
    ------------
    1100 = 12

**Right shift operator**

    num = 8

    #RIGHT SHIFT - Shifting Bit to Rightmost
    print( num>>3 )

 Output

    1

The result is 1, since the bits are pushing from right to left (3 places movement since we gave <<3)

    1000 = 8
    >>3
    -------------
    0001 = 1