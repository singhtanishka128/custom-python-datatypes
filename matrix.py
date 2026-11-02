from typing import List


class Matrix:
  """Represents a 2D Matrix supporting linear algebra operations"""

  def __init__(self, data: List[List[float]]):
    if not data or not data[0]:
      raise ValueError("Matrix cannot be empty.")
    row_len = len(data[0])
    if any(len(row) != row_len for row in data):
      raise ValueError("All rows must have the same length.")
    self.data = data
    self.rows = len(data)
    self.cols = row_len

  def __str__(self) -> str:
    return "\n".join(str(row) for row in self.data)

  def __add__(self, other: "Matrix") -> "Matrix":
    if self.rows != other.rows or self.cols != other.cols:
      raise ValueError("Matrices must have the same dimensions for addition.")
    new_data = [
      [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
      for i in range(self.rows)
    ]
    return Matrix(new_data)

  def __matmul__(self, other: "Matrix") -> "Matrix":
    if self.cols != other.rows:
      raise ValueError(
          "Columns of first matrix must match rows of second matrix."
      )
    result = [[0.0] * other.cols for _ in range(self.rows)]
    for i in range(self.rows):
      for j in range(other.cols):
        for k in range(self.cols):
          result[i][j] += self.data[i][k] * other.data[k][j]
    return Matrix(result)

  def transpose(self) -> "Matrix":
    transposed_data = [
      [self.data[j][i] for j in range(self.rows)] for i in range(self.cols)
    ]
    return Matrix(transposed_data)