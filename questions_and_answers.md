# Game Character Stats Tracker - Questions and Answers

## 20 Questions About Getters, Setters, and Properties in Python

### 1. What is a property in Python?
**Answer:** A property in Python is a way to define getters, setters, and deleters for class attributes using the `@property` decorator. It allows you to access methods like attributes, providing a clean interface while maintaining encapsulation and allowing for data validation.

### 2. What is the difference between a getter and a setter?
**Answer:** A getter retrieves the value of an attribute, while a setter sets or updates the value of an attribute. Getters use the `@property` decorator, and setters use the `@property_name.setter` decorator. Getters allow read access, while setters allow write access with validation.

### 3. Why do we use underscore prefixes (e.g., `_name`, `_health`) for private attributes?
**Answer:** In Python, the underscore prefix (`_`) is a convention indicating that an attribute or method is intended for internal use within the class. It signals to other developers that these attributes should not be accessed directly from outside the class, promoting encapsulation and data protection.

### 4. What happens if you try to set a property that only has a getter defined (read-only property)?
**Answer:** If you try to set a read-only property (one that only has a `@property` getter without a setter), Python will raise an `AttributeError: can't set attribute`. This prevents accidental modification of the attribute.

### 5. How does the `@property` decorator work?
**Answer:** The `@property` decorator converts a method into a property getter. When you access the property (e.g., `character.health`), Python automatically calls the decorated method instead of directly accessing an attribute, allowing you to perform validation or computation.

### 6. What is the purpose of using setters in Python?
**Answer:** Setters allow you to validate, transform, or control how attributes are set. They provide a way to enforce constraints (like capping values within a range), log changes, trigger side effects, or perform data validation before storing values.

### 7. In the GameCharacter class, why does `health` have both a getter and a setter, while `name` only has a getter?
**Answer:** `health` needs a setter to enforce validation rules (must be between 0 and 100). `name` only has a getter because it's meant to be read-only—once a character is created, their name shouldn't change, so there's no setter defined.

### 8. What is the difference between `self._health` and `self.health`?
**Answer:** `self._health` directly accesses the private attribute, bypassing any getter/setter logic. `self.health` uses the property, which calls the getter method (or setter if assigning). Using the property ensures validation and encapsulation.

### 9. Why do we use `self.health = 100` instead of `self._health = 100` in the `level_up` method?
**Answer:** We use `self.health = 100` to take advantage of the setter's validation logic. If we directly set `self._health = 100`, we bypass the setter. While 100 is valid, using the property is a best practice because if the validation logic changes, the code will still work correctly.

### 10. Can you have a property without a getter in Python?
**Answer:** No, you cannot have a property without a getter. The `@property` decorator creates the getter. However, you can make a property effectively write-only by raising an `AttributeError` in the getter, though this is uncommon and not recommended.

### 11. What is method resolution order when using properties?
**Answer:** When you access `object.property`, Python first checks for a property with that name. If a property exists, it calls the getter method. If you assign `object.property = value`, Python checks for a setter. If no property exists, Python looks for a regular attribute.

### 12. How do you create a read-only property in Python?
**Answer:** To create a read-only property, define only the getter using `@property` without defining a setter. If someone tries to set it, Python will raise an `AttributeError`. This is what we did with the `name` property in GameCharacter.

### 13. What is the `__str__` method used for?
**Answer:** The `__str__` method defines the string representation of an object. It's called by the `print()` function and `str()` built-in function. It should return a human-readable string representation of the object.

### 14. Why do we use private attributes (`_health`, `_mana`) instead of public attributes (`health`, `mana`)?
**Answer:** Using private attributes prevents direct external access, forcing code to use properties (getters/setters). This ensures data validation, maintains encapsulation, allows for future changes to internal implementation, and prevents accidental invalid data assignments.

### 15. Can a setter access other properties or methods?
**Answer:** Yes, a setter can access other properties and methods using `self`. For example, a setter could call other methods, modify other attributes, or perform calculations based on other properties. This allows for complex validation and side effects.

### 16. What is the difference between `@property` and `@staticmethod`?
**Answer:** `@property` converts a method to a property that works with an instance (takes `self`), while `@staticmethod` creates a method that doesn't require an instance (no `self` parameter). Properties are instance-specific, while static methods are not tied to any instance.

### 17. How do property decorators help with backward compatibility?
**Answer:** If you start with a public attribute and later need to add validation, you can convert it to a property without changing the external interface. Code that accessed `obj.attribute` will continue to work, but now goes through getters/setters, maintaining backward compatibility.

### 18. In the health setter, what happens if someone tries to set health to -50?
**Answer:** The setter checks if the value is less than 0 and sets `self._health = 0` instead. This prevents invalid negative health values and ensures the health always stays within valid bounds (0 to 100).

### 19. What is encapsulation and how do properties help achieve it?
**Answer:** Encapsulation is the principle of bundling data and methods together and restricting direct access to internal state. Properties help achieve encapsulation by allowing controlled access through getters and setters, hiding the internal representation (`_attribute`) while providing a clean interface (`attribute`).

### 20. Can you delete a property? How?
**Answer:** Yes, you can define a deleter for a property using `@property_name.deleter`. When you use `del object.property`, Python calls the deleter method. If no deleter is defined, attempting to delete will raise an `AttributeError: can't delete attribute`.