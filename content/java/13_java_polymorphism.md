# Polymorphism in Java

Polymorphism means "many forms". In Java, it allows objects to be treated as instances of their parent class rather than their actual class.

## Types of Polymorphism
- **Compile-time (Method Overloading)**
- **Runtime (Method Overriding)**

## Method Overloading Example
```java
class MathUtils {
    int add(int a, int b) {
        return a + b;
    }
    double add(double a, double b) {
        return a + b;
    }
}
```

## Method Overriding Example
```java
class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Bark");
    }
}

Animal a = new Dog();
a.sound(); // Output: Bark
```
