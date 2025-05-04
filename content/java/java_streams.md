# Streams API in Java

Streams provide a modern way to process collections of objects in a functional style.

## Example
```java
import java.util.*;
import java.util.stream.*;
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
int sum = numbers.stream().filter(n -> n % 2 == 0).mapToInt(n -> n).sum();
System.out.println(sum); // 6
```

## Common Stream Operations
- `filter`
- `map`
- `reduce`
- `collect`
- `forEach`
