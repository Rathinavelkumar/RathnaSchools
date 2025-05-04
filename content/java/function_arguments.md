# Method Arguments in Java

Arguments are values passed to methods when they are called.

## Example
```java
public void printMessage(String message) {
    System.out.println(message);
}

printMessage("Hello Java!");
```

## Pass by Value
- In Java, method arguments are always passed by value.
- For objects, the reference is passed by value.

## Varargs (Variable Arguments)
```java
public void printNumbers(int... nums) {
    for (int n : nums) {
        System.out.println(n);
    }
}

printNumbers(1, 2, 3, 4);
```
