import numpy as np


def euclidean_distance(p, q):
    p = np.array(p)
    q = np.array(q)

    print(f"\nPoint p: {p}")
    print(f"Point q: {q}")

    diff = p - q
    print(f"\nDifferences (p - q): {diff}")

    squared = diff ** 2
    print(f"Squared: {squared}")

    sum_sq = np.sum(squared)
    print(f"Sum: {sum_sq}")

    distance = np.sqrt(sum_sq)
    print(f"\nDistance = √{sum_sq} = {distance:.4f}")

    return distance


print("=" * 50)
print("EUCLIDEAN DISTANCE CALCULATOR")
print("=" * 50)

print("\n[Example 1] 2D: A(2,3) to B(5,7)")
d1 = euclidean_distance([2, 3], [5, 7])

print("\n" + "=" * 50)
print("\n[Example 2] 3D: P(1,2,3) to Q(4,6,8)")
d2 = euclidean_distance([1, 2, 3], [4, 6, 8])

print("\n" + "=" * 50)
print("\n[Example 3] Origin to (6,8)")
d3 = euclidean_distance([0, 0], [6, 8])

print("\n" + "=" * 50)