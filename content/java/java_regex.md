# Regular Expressions in Java

Regular expressions (regex) are used for pattern matching in strings.

## Example
```java
import java.util.regex.*;
String text = "My phone: 123-456-7890";
Pattern pattern = Pattern.compile("\\d{3}-\\d{3}-\\d{4}");
Matcher matcher = pattern.matcher(text);
if (matcher.find()) {
    System.out.println("Found: " + matcher.group());
}
```
