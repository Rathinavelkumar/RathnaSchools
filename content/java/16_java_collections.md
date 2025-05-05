# Collections in Java

Java Collections Framework provides classes and interfaces for storing and manipulating groups of data.

## List Example
```java
import java.util.*;
List<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
System.out.println(names.get(0)); // Alice
```

## Set Example
```java
Set<Integer> numbers = new HashSet<>();
numbers.add(1);
numbers.add(2);
numbers.add(1); // Duplicate will not be added
```

## Map Example
```java
Map<String, Integer> ages = new HashMap<>();
ages.put("Alice", 30);
ages.put("Bob", 25);
System.out.println(ages.get("Alice")); // 30
```
