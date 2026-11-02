from typing import Union


class Interval:
  """Represents a continuous numerical range [low, high]"""

  def __init__(self, low: float, high: float):
    if low > high:
      raise ValueError("Lower bound cannot be greater than upper bound.")
    self.low = low
    self.high = high

  def __str__(self) -> str:
    return f"[{self.low}, {self.high}]"

  def __contains__(self, value: float) -> bool:
    return self.low <= value <= self.high

  def overlaps(self, other: "Interval") -> bool:
    return max(self.low, other.low) <= min(self.high, other.high)

  def intersection(self, other: "Interval") -> Union["Interval", None]:
    if not self.overlaps(other):
      return None
    return Interval(max(self.low, other.low), min(self.high, other.high))