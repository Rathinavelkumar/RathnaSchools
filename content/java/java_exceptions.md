# Exception Handling in Java

Exceptions are events that disrupt the normal flow of a program. Java provides a robust mechanism to handle exceptions.

## Types of Exceptions
- **Checked Exceptions**: Must be handled or declared (e.g., IOException)
- **Unchecked Exceptions**: Runtime exceptions (e.g., NullPointerException)

## try-catch Block
```java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
}
```

## finally Block
```java
try {
    // code
} finally {
    // always executed
}
```

## throw and throws
```java
public void checkAge(int age) throws Exception {
    if (age < 18) {
        throw new Exception("Underage");
    }
}
```
