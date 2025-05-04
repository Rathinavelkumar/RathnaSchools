# Lambda Expressions in Java

Lambdas provide a clear and concise way to represent one method interface using an expression.

## Syntax
```java
(parameter_list) -> { // body }
```

## Example
```java
interface MathOperation {
    int operation(int a, int b);
}

MathOperation add = (a, b) -> a + b;
System.out.println(add.operation(5, 3)); // 8
```

## Using Lambdas with Collections
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
names.forEach(name -> System.out.println(name));
```
