"""
Demonstrate arithmetic and comparison operators in Python
"""

a = 99
b = 23
u = 89
x = 50
y = 78
t = 1

# ── Arithmetic operators ─────────────────────────────
print("Addition (+)        :", t + a)        # 1 + 99  = 100
print("Subtraction (-)     :", a - u)        # 99 − 89 = 10
print("Division (/)        :", x / y)        # 50 / 78 ≈ 0.641
print("Floor division (//) :", x // y)       # 0  (quotient only)
print("Multiplication (*)  :", a * b)        # 99 × 23 = 2277
print("Modulus (%)         :", a % b)        # 99 mod 23 = 7
print("Exponent (** )      :", b ** t)       # 23 ** 1 = 23

# ── Comparison operators ─────────────────────────────
print("Equal (==)          :", u == t)       # False
print("Not equal (!=)      :", u != t)       # True
print("Greater than (>)    :", a > b)        # True
print("Less than (<)       :", x < a)        # True
print("Greater-or-equal (>=):", a >= 99)     # True
print("Less-or-equal (<=)  :", y <= x)       # False
