import numpy as np


def manhattan_distance(p, q):
    p = np.array(p)
    q = np.array(q)

    print(f"\nPoint p: {p}")
    print(f"Point q: {q}")

    diff = np.abs(p - q)
    print(f"\nAbsolute differences |p - q|: {diff}")

    distance = np.sum(diff)
    print(f"\nManhattan Distance = {' + '.join(map(str, diff))} = {distance}")

    return distance


print("=" * 50)
print("MANHATTAN DISTANCE CALCULATOR")
print("=" * 50)

print("\n[Example 1] A(2,3) to B(5,7)")
d1 = manhattan_distance([2, 3], [5, 7])

print("\n" + "=" * 50)
print("\n[Example 2] P(1,2,3) to Q(4,6,8)")
d2 = manhattan_distance([1, 2, 3], [4, 6, 8])

print("\n" + "=" * 50)
print("\n[Example 3] Origin to (6,8)")
d3 = manhattan_distance([0, 0], [6, 8])

print("\n" + "=" * 50)