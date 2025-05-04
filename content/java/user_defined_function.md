# Methods (Functions) in Java

A method is a block of code that performs a specific task. Methods are defined inside classes.

## Defining a Method
```java
public int add(int a, int b) {
    return a + b;
}
```

## Calling a Method
```java
int result = add(5, 3); // result = 8
```

## Static Methods
```java
public static void greet() {
    System.out.println("Hello!");
}

greet(); // Call without creating an object
```
