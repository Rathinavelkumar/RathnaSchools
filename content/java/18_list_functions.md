# List Methods in Java

Lists in Java (via ArrayList) have useful methods for manipulation.

## Example
```java
import java.util.*;
List<Integer> nums = new ArrayList<>();
nums.add(10);
nums.add(20);
nums.add(30);
System.out.println(nums.size()); // 3
System.out.println(nums.contains(20)); // true
nums.remove(1); // removes 20
System.out.println(nums); // [10, 30]
```
