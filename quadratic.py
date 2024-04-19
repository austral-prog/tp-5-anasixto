import math
def roots(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante))/2*a
        r2 = (-b - math.sqrt(discriminante))/2*a
        return f"{r1}, {r2}"
    elif discriminante == 0
        r1 = (-b)/2*a
        return f"{r1}"
    else:
        return "()"
        


def value_y(a, b, c, x):
    y = a*(X**2)+b*X+c
    return f"{y}"


def to_string(a, b, c):
    return f"f(x) = {a} * (x**2) + {b}*X + {c}"


def derivation(a, b):
    return f"f(x) = 2*{a}*X + {b}"
