class Distance:
  """Represents a physical distance with automatic unit conversion"""

  CONVERSIONS = {
      "mm": 0.001,
      "cm": 0.01,
      "m": 1.0,
      "km": 1000.0,
      "in": 0.0254,
      "ft": 0.3048,
      "mi": 1609.34,
  }

  def __init__(self, value: float, unit: str = "m"):
    if unit not in self.CONVERSIONS:
      raise ValueError(f"Invalid unit. Choose from {list(self.CONVERSIONS.keys())}")
    self.value = value
    self.unit = unit

  def to_meters(self) -> float:
    return self.value * self.CONVERSIONS[self.unit]

  def to(self, target_unit: str) -> "Distance":
    if target_unit not in self.CONVERSIONS:
      raise ValueError("Invalid target unit.")
    meters = self.to_meters()
    new_value = meters / self.CONVERSIONS[target_unit]
    return Distance(new_value, target_unit)

  def __str__(self) -> str:
    return f"{self.value} {self.unit}"

  def __add__(self, other: "Distance") -> "Distance":
    total_meters = self.to_meters() + other.to_meters()
    return Distance(total_meters / self.CONVERSIONS[self.unit], self.unit)