# Basic eucledian algorithm to find the greatest common divisor of 2 numbers


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
x=raw_input()
y=raw_input()

print(gcd(x, y))
