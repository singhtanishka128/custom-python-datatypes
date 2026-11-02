from typing import List


class Polynomial:
  """Represents a polynomial expression, e.g., 3x^2 + 2x + 5 stored as [3, 2, 5]"""

  def __init__(self, coefficients: List[float]):
    while len(coefficients) > 1 and coefficients[0] == 0:
      coefficients.pop(0)
    self.coefficients = coefficients

  def __str__(self) -> str:
    degree = len(self.coefficients) - 1
    terms = []
    for i, coeff in enumerate(self.coefficients):
      if coeff == 0:
        continue
      deg = degree - i
      if deg > 1:
        terms.append(f"{coeff}x^{deg}")
      elif deg == 1:
        terms.append(f"{coeff}x")
      else:
        terms.append(f"{coeff}")
    return " + ".join(terms) if terms else "0"

  def __call__(self, x: float) -> float:
    result = 0.0
    for coeff in self.coefficients:
      result = result * x + coeff
    return result

  def __add__(self, other: "Polynomial") -> "Polynomial":
    diff = len(self.coefficients) - len(other.coefficients)
    p1 = [0] * max(0, -diff) + self.coefficients
    p2 = [0] * max(0, diff) + other.coefficients
    new_coeffs = [a + b for a, b in zip(p1, p2)]
    return Polynomial(new_coeffs)