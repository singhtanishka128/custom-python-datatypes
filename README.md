# Custom Python Datatypes

A lightweight Python library demonstrating **Object-Oriented Programming (OOP), operator overloading, and custom mathematical data structures**, built completely from scratch without relying on external third-party libraries.

This project showcases Python fundamentals, magic methods (`__init__`, `__add__`, `__matmul__`, `__contains__`, `__call__`), and clean software architecture through the implementation of custom mathematical datatypes.

---

## Project Structure

```text
custom_python_datatype/
│
├── complex_number.py   # Complex numbers (a + bi) with arithmetic & magnitude
├── matrix.py           # 2D Matrix supporting addition, transpose, and multiplication
├── interval.py         # Continuous numerical ranges with overlap & membership checks
├── polynomial.py       # Algebraic expressions with Horner's method evaluation
├── distance.py         # Physical quantities with automatic multi-unit conversion
└── demo.ipynb          # Interactive Jupyter Notebook demonstrating usage
```

---

## Implemented Datatypes

### 1. ComplexNumber (`complex_number.py`)

Handles complex number arithmetic, magnitude calculation, and division using conjugates.

**Example:**

```python
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print(c1 + c2)  # 4 + 9i
print(abs(c1))  # 3.605...
```

### 2. Matrix (`matrix.py`)

Implements 2D linear algebra operations, supporting matrix addition, transpose, and matrix multiplication using Python's native `@` operator through the `__matmul__` magic method.

**Example:**

```python
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print(m1 @ m2)
```

### 3. Interval (`interval.py`)

Represents continuous numerical ranges `[low, high]`. Overloads the `in` operator using `__contains__` and supports range overlap and intersection checks.

**Example:**

```python
i = Interval(1, 5)

print(3 in i)  # True
```

### 4. Polynomial (`polynomial.py`)

Represents algebraic expressions stored as coefficient lists. Overloads the `__call__` magic method, allowing instances to be evaluated like functions using Horner's method.

**Example:**

```python
poly = Polynomial([3, 2, 5])  # 3x² + 2x + 5

print(poly(2))  # Evaluates at x = 2 -> 21
```

### 5. Distance (`distance.py`)

Encapsulates physical measurements with automatic unit conversions across millimeters, meters, kilometers, inches, feet, and miles.

**Example:**

```python
d1 = Distance(5, "m")
d2 = Distance(10, "ft")

print(d1 + d2)  # Automatically converts units and adds them
```

---

## Python Concepts Demonstrated

* **Object-Oriented Programming:** Classes, objects, constructors, and encapsulation.
* **Magic Methods:** Customizing built-in Python operations.
* **Operator Overloading:** Implementing operators such as `+` and `@`.
* **Membership Testing:** Customizing the `in` operator.
* **Callable Objects:** Making class instances behave like functions.
* **Algorithm Implementation:** Using Horner's method for polynomial evaluation.
* **Clean Code Structure:** Organizing implementations into separate Python modules.

---

## How to Run the Demo

1. Clone or download this repository.
2. Open the project folder in an IDE such as VS Code or launch Jupyter Notebook from your terminal.
3. Open `demo.ipynb`.
4. Run the notebook cells to explore the implementation and usage of all five custom datatypes.

---

## Project Objective

The objective of this project is to strengthen Python programming fundamentals by implementing custom datatypes and understanding how Python's object model allows developers to define custom behavior for built-in operations.

All implementations are developed from scratch without relying on external third-party libraries.
