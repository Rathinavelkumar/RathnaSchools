# Generics in Java

Generics allow classes and methods to operate on objects of various types while providing compile-time type safety.

## Example: Generic Class
```java
class Box<T> {
    private T value;
    public void set(T value) { this.value = value; }
    public T get() { return value; }
}

Box<Integer> intBox = new Box<>();
intBox.set(123);
System.out.println(intBox.get()); // 123
```

## Example: Generic Method
```java
public <T> void printArray(T[] array) {
    for (T elem : array) {
        System.out.println(elem);
    }
}
```
