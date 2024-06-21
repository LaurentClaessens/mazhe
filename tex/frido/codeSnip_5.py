import random


def f1(z1: complex, z2: complex, r: float) -> float:
    return abs((z1+z2)/2)**r


def f2(z1: complex, z2: complex, r: float) -> float:
    return (abs(z1)**r + abs(z2)**r)/2


def test(z1: complex, z2: complex, r: float) -> float:
    """Should be positive."""
    return f2(z1, z2, r) - f1(z1, z2, r)


for _ in range(1, 10):
    r = random.uniform(1, 1.3)
    x1 = random.uniform(-10, 10)
    y1 = random.uniform(-10, 10)
    x2 = random.uniform(-10, 10)
    y2 = random.uniform(-10, 10)
    z1 = complex(x1, y1)
    z2 = complex(x2, y2)
    result = test(z1, z2, r)
    print("-----")
    print(f"z1={z1}")
    print(f"z2={z2}")
    print(f"r={r}")
    print("---> ", result)
    if result < 0:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
