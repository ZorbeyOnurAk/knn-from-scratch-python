# k-NN From Scratch in Python

This project implements a simple k-Nearest Neighbors classifier using plain Python without machine learning libraries.

## What this project does

Given a query point, the program:

1. Calculates Euclidean distance to every training point
2. Sorts the distances
3. Selects the k nearest neighbors
4. Collects their labels
5. Predicts the most common label

## Example dataset

```python
data = [
    ([1, 1], "Red"),
    ([2, 1], "Red"),
    ([2, 2], "Red"),
    ([6, 6], "Blue"),
    ([7, 6], "Blue"),
    ([6, 7], "Blue")
]

query = [3, 2]
k = 3
