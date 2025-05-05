# Special Parameters in Java Methods

## The `this` Keyword
- Refers to the current object.
```java
public class Car {
    private String model;
    public Car(String model) {
        this.model = model;
    }
}
```

## Final Parameters
- A method parameter can be declared as `final` to prevent modification.
```java
public void print(final int x) {
    // x cannot be changed inside this method
    System.out.println(x);
}
```
