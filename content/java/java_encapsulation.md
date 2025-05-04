# Encapsulation in Java

Encapsulation is the process of wrapping data (variables) and code (methods) together as a single unit. It restricts direct access to some of the object's components.

## Example
```java
public class Person {
    private String name; // private variable
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}

Person p = new Person();
p.setName("Alice");
System.out.println(p.getName());
```

- Use `private` for fields
- Use `public` getters and setters to access and update fields
