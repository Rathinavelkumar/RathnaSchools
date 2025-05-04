# Abstraction in Java

Abstraction is the concept of hiding complex implementation details and showing only the essential features of an object.

## Abstract Classes
- Cannot be instantiated directly
- May contain abstract methods (without body)

```java
abstract class Animal {
    abstract void sound(); // Abstract method
    void eat() {
        System.out.println("Eating...");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Bark");
    }
}

Animal a = new Dog();
a.sound(); // Output: Bark
a.eat();   // Output: Eating...
```

## Interfaces
- Defines a contract that implementing classes must follow

```java
interface Drawable {
    void draw();
}

class Circle implements Drawable {
    public void draw() {
        System.out.println("Drawing Circle");
    }
}

Drawable d = new Circle();
d.draw(); // Output: Drawing Circle
```
