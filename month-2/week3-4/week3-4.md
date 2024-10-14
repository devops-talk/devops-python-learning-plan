# Python OOP and Recursion Practice Problems

This set of problems focuses on **Object-Oriented Programming (OOP)** and **Recursion** concepts. The problems are designed for a DevOps engineer looking to enhance their Python skills, particularly in areas related to automation and problem-solving.

## Object-Oriented Programming (OOP) Problems

### 1. Basic Class and Object
- **Problem**: Create a class `Car` with attributes like `make`, `model`, and `year`. Add methods to:
  - Print car details.
  - Check if the car is old (older than 10 years).
- **Objective**: Understand basic class structure, attributes, and methods.

### 2. Class Inheritance
- **Problem**: Create a base class `Device` with attributes `name` and `status`. Derive a class `Smartphone` that adds the attribute `apps`. Add methods to:
  - Display the device details.
  - Install apps on the smartphone.
- **Objective**: Learn about inheritance and method overriding.

### 3. Polymorphism
- **Problem**: Implement two classes, `Dog` and `Cat`, each with a `make_sound()` method that prints the respective sound the animal makes. Write a function that accepts objects of either class and calls `make_sound()`.
- **Objective**: Practice polymorphism by overriding methods in different classes.

### 4. AWS Resource Management (Class-Based)
- **Problem**: Create a class `AWSResourceManager` that has methods to:
  - `start_instance()`
  - `stop_instance()`
  - `list_resources()`
  - Simulate managing mock AWS resources.
- **Objective**: Use OOP principles to simulate AWS resource management, which is relevant to DevOps tasks.

### 5. Bank Account Simulation
- **Problem**: Create a class `BankAccount` with methods to:
  - `deposit(amount)`
  - `withdraw(amount)`
  - `get_balance()`
  - Ensure that withdrawals do not result in a negative balance.
- **Objective**: Understand how to implement simple class-based simulations.

---

## Recursion Problems

### 6. Factorial Calculation (Recursive)
- **Problem**: Write a recursive function `factorial(n)` that computes the factorial of a given number `n`.
- **Objective**: Practice recursion with a classic mathematical problem.

### 7. Fibonacci Sequence (Recursive)
- **Problem**: Write a recursive function `fibonacci(n)` to calculate the `n`-th number in the Fibonacci sequence. Implement memoization to avoid repeated calculations.
- **Objective**: Practice recursion and optimize it with memoization techniques.

### 8. Sum of Digits (Recursive)
- **Problem**: Implement a recursive function `sum_of_digits(n)` to compute the sum of digits of a given integer `n`.
- **Objective**: Solve a simple problem using recursion.

### 9. Find Maximum in List (Recursive)
- **Problem**: Write a recursive function `find_max(lst)` that finds the maximum value in a list of integers `lst`.
- **Objective**: Use recursion to process lists and find a solution.

### 10. Recursive Directory Search
- **Problem**: Write a recursive function `search_file(directory, filename)` that searches for a specific file in a directory and its subdirectories.
- **Objective**: Use recursion to traverse directories, a relevant task for file management in DevOps.
  
---

## How to Use
1. Start with the OOP problems, implement each class and method step-by-step.
2. Move on to recursion problems to get comfortable with breaking problems into smaller, self-referential solutions.
3. Use Python IDEs or Jupyter Notebooks to test your solutions.

Happy Coding!
