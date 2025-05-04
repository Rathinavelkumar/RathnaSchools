# Inheritance in Java

Inheritance allows a class to acquire the properties and methods of another class.

## Example
```java
class Animal {
    void eat() {
        System.out.println("Eating...");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking...");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();  // Inherited method
        d.bark(); // Own method
    }
}
```

## Types of Inheritance
- Single Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance

> Note: Java does not support multiple inheritance with classes (can be achieved with interfaces).
