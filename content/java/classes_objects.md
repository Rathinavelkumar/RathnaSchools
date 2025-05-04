# Classes and Objects in Java

Java is an object-oriented language. Everything revolves around classes and objects.

## Defining a Class
```java
public class Animal {
    String name;
    void speak() {
        System.out.println("Animal speaks");
    }
}
```

## Creating Objects
```java
Animal dog = new Animal();
dog.name = "Buddy";
dog.speak();
```

## Constructors
```java
public class Person {
    String name;
    public Person(String n) {
        name = n;
    }
}

Person p = new Person("Alice");
```
