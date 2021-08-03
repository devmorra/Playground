#!/usr/bin/env python

DIGITS = 100

def pi_digits(x):
    """Generate x digits of Pi."""
    k,a,b,a1,b1 = 2,4,1,12,4
    while x > 0:
        p,q,k = k * k, 2 * k + 1, k + 1
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d,d1 = a/b, a1/b1
        while d == d1 and x > 0:
            yield int(d)
            x -= 1
            a,a1 = 10*(a % b), 10*(a1 % b1)
            d,d1 = a/b, a1/b1

digits = [str(n) for n in list(pi_digits(DIGITS))]
print(digits)
#print("%s.%s\n" % (digits.pop(0), "".join(digits)))
print(f"{digits[0]}.{''.join(digits[1:])}")
print(f"{digits.pop(0)}.{''.join(digits)}")
print(digits)
#print(pi_digits(10))