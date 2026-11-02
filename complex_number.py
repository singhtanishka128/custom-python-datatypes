class ComplexNumber:
  """Represents a complex number: a + bi"""

  def __init__(self, real: float, imag: float):
    self.real = real
    self.imag = imag

  def __str__(self) -> str:
    sign = "+" if self.imag >= 0 else "-"
    return f"{self.real} {sign} {abs(self.imag)}i"

  def __repr__(self) -> str:
    return f"ComplexNumber({self.real}, {self.imag})"

  def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
    return ComplexNumber(self.real + other.real, self.imag + other.imag)

  def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
    return ComplexNumber(self.real - other.real, self.imag - other.imag)

  def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
    r = self.real * other.real - self.imag * other.imag
    i = self.real * other.imag + self.imag * other.real
    return ComplexNumber(r, i)

  def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
    denom = other.real**2 + other.imag**2
    if denom == 0:
      raise ZeroDivisionError("Division by zero complex number.")
    r = (self.real * other.real + self.imag * other.imag) / denom
    i = (self.imag * other.real - self.real * other.imag) / denom
    return ComplexNumber(r, i)

  def __abs__(self) -> float:
    return (self.real**2 + self.imag**2) ** 0.5