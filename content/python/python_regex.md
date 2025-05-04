**Reg**ular **Ex**pression is shortly called as RegEx which helps to search a string which contain the specified search pattern. `re` module helps to perform regex operations in python

## Metacharacters
Metacharacters are used to specify the regular expressions. The list of metacharacters are **`[]{}()\|.?$^*+`**. Each character's usage explained in the below sections

`Note` : `https://pythex.org/` is a best website to test the regular expressions

## Square Brackets [ ]

With the help of square bracket, we can specify a set of characters to match with the given string

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
|  | a | 1 Match |
|  | au | 2 Matches |
| [aeiou] | rathna schools | 4 Matches |
|  | myth | No Match |
|  | ieauo | 5 Matches |

* We can specify the range of characters using - such as [a-e] is consider as [abcde]
* similarly [0-5] is consider as [012345]
* Complement operators inverse the character list such as [^a] is consider as any characters except a
* similarly [^0-9] is consider as any non digit characters

## Period .
1 period matches 1 characters incase 2 period means, it wil match 2 characters and so on. But, it won't consider the  newline \n

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **.** | a | 1 Match |
| **..** | au | 2 Matches |
| **.** | rathnaschools | 13 Matches |
| **..** | rathnaschools | 6 Matches |
| **...** | ieauo | 1 match |

## Caret ^
Caret symbol is used to check the prefix of the given string and returns whether it match or not

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **^a** | rathnaschools | No match |
| **^r** | au | Match |
| **^R** | rathnaschools | No match |
| **^rs** | rathnaschools | No match |
| **^ra** | rathnaschools | match |

## Dollar $
Dollar symbol is used to check the suffix of the given string and returns whether it match or not

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **a$** | rathnaschools | No match |
| **s$** | au | Match |
| **S$** | rathnaschools | No match |
| **rs$** | rathnaschools | No match |
| **ls$** | rathnaschools | match |

## Star *
Star symbol used to match the zero or multiple occurrences of the pattern left to the given string

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **pytho*n** | pythn | Match |
| **pytho*n** | python | Match |
| **pytho*n** | pythoooon | Match |
| **pytho*n** | pythoan | No match |
| **pytho*n** | learnpython | match |

## Plus +
Plus symbol used to match the zero or multiple occurrences of the pattern right to the given string

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **pytho+n** | pythn | No match |
| **pytho+n** | python | Match |
| **pytho+n** | pythoooon | Match |
| **pytho+n** | pythoan | No match |
| **pytho+n** | pythonlearn | match |

## Question Mark ?
Question Mark symbol used to match the zero or multiple occurrences of the pattern left to the given string

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **pytho?n** | pythn | Match |
| **pytho?n** | python | Match |
| **pytho?n** | pythoooon | No Match (more than one 'o') |
| **pytho?n** | pythoan | No match |
| **pytho?n** | learnpython | match |

## Braces { }
Braces are used to find the repetitive pattern in the given string with {at least, at most} specifications. example if it {2, 3} means minimum two time character should repeat and at most three time in the given string

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **o{2,3}** | verbose | No Match |
| **o{2,3}** | verboose | Match |
| **o{2,3}** | verboose schools | 2 Match |
| **o{2,3}** | verbooose schools | 2 Match |
| **o{2,3}** | verbooooose schools | 3 Match |

## Vertical Bar |
Vertical bar | performs the same operation of OR operators in programming language

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **p\|o** | python | 2 match |
| **p\|o** | learn | No Match |
| **p\|o** | python python | 4 Match |

## Parentheses ( )
Parentheses are used to match the sub-patterns in the given input string

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| (a\|h\|n)on | python | 1 match |
| (a\|e\|n)on | python | No Match |
| (a\|h\|r)on | learon python | 2 Match |

## Backslash
Backslash is act as an escape characters including all metacharacters. If we want to search $50 in the given string means, we need to skip the $ symbol like below

| Expression | String | Number of Matches |
| :------------ |-----: |-----: |
| **$50** | The balance is $50. | No match |
| **\$50** | The balance is $50. | 1 Match |


## Special Sequence
The regularly using patterns can be easily written with special sequence. The list of special sequences are

| Expression | Description | String | Number of Matches |
| :------------ |-----: |-----: |-----: |
| \Alearn | Check the start of the string | learn python | 1 Match |
| python\Z | Check the end of the string | learn python | 1 Match |
| \blearn | Check the start of the string | learn python | 1 Match |
| python\b | Check the end of the string | learn python | 1 Match |
| \Blearn | Check the not start of the string | learn python | No Match |
| python\B | Check the not end of the string | learn python | No Match |
| \d | returns the integers in the string | learn python 123 | 123 |
| \D | returns the non integers in the string | learn python 123 | learn python |
| \s | returns the white space in the string | learn python | 2 white spaces |
| \S | returns the non white space in the string | learn python | learnpython123 |
| \w | returns the alpha numeric in the string | learn python 123 | learnpython123 |
| \W | returns the non alpha numeric in the string | learn python 123 | 2 white spaces |

## re findall method
Findall method in re module helps to return the matching pattern in the given string

    import re

    input_data = "Learn 123 python 456"
    pattern = "\d+"

    result = re.findall(pattern, input_data)
    print(result)

 Output

    ['123', '456']

## re split method
Split method in re module helps to split the string based on the matching pattern in the given string

    import re

    input_data = "Learn 123 python 456"
    pattern = "\d+"

    result = re.split(pattern, input_data)
    print(result)

 Output

    ['Learn ', ' python ', '']

## re sub method
Sub method in re module helps to replace the string based on the matching pattern in the given string

    import re

    input_data = "Learn 123 python 456"
    pattern = "\d+"
    replace = "***"

    result = re.sub(pattern, replace, input_data)
    print(result)

 Output

    Learn *** python ***

## re subn method
Subn method in re module helps to replace the string based on the matching pattern and also returns the count of number of occurrence in the given string

    import re

    input_data = "Learn 123 python 456"
    pattern = "\d+"
    replace = "***"

    result = re.subn(pattern, replace, input_data)
    print(result)

 Output

    ('Learn *** python ***', 2)

## re search method
Search method in re module helps to search the string based on the matching pattern and returns none if the pattern is not available in the given string

    import re

    input_data = "Learn 123 python 456"
    pattern = "\d+"

    result = re.search(pattern, input_data)
    if result:
        print("Integer available in the given string")
    else:
        print("No integer in the given string")

 Output

    Integer available in the given string