# The differences between Java and Python
1. Truthiness: inferred in Python, for example and empty list is falsy and is often used in 'if' conditions i.e. if not list:
2. No automatic int -> string conversion: important for inputs which are taken as a string, need to convert to int i.e. int(s) or str(i) - other way
3. snake_case: Java uses camelCase, Python uses snake_case
4. Function scope instead of block scope: variables survive if/for/with, when in Java they would be contained to those scopes.
5. Mutable default arguments: A default is shared between instances, not created fresh each instance like Java. Fix is to use dataclasse with field(default_factory=list) or none as a sentinel
6. == vs is: == compares value, is compares object location, opposite of Java equal() compares value and == compares object location
7. Comprehensions: [x for x in items if condition] - creates a new list by iterating through another list. Comprehensions work over any iterable
8. Ducktyping: Java enforces the declared type at the call site, Python does not. It checks the method and if it doesn't exist returns an error
