"""
Equation Solver
Supports:
  - Linear equations:    ax + b = 0
  - Quadratic equations: ax² + bx + c = 0
"""

import math


def solve_linear(a, b):
    """Solve ax + b = 0.  Returns the single root, or None if no solution."""
    if a == 0:
        return None  # 0x + b = 0 has no unique solution
    return -b / a


def solve_quadratic(a, b, c):
    """Solve ax² + bx + c = 0.
    Returns a tuple of roots (real or complex).
    """
    if a == 0:
        root = solve_linear(b, c)
        return (root,) if root is not None else ()

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminant) / (2 * a)
        return (complex(real, imag), complex(real, -imag))


def main():
    print("=== Equation Solver ===")
    print("1. Linear equation    (ax + b = 0)")
    print("2. Quadratic equation (ax² + bx + c = 0)")
    choice = input("Choose equation type (1 or 2): ").strip()

    if choice == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        root = solve_linear(a, b)
        if root is None:
            print("No unique solution (a = 0).")
        else:
            print(f"Solution: x = {root}")

    elif choice == "2":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        roots = solve_quadratic(a, b, c)
        if not roots:
            print("No solution.")
        elif len(roots) == 1:
            print(f"One root: x = {roots[0]}")
        else:
            print(f"Two roots: x₁ = {roots[0]},  x₂ = {roots[1]}")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
