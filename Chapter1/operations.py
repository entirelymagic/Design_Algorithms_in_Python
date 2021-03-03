from Chapter1.def_rational_numbers import Rational


"""Operations performed with rational numbers"""


print(Rational.processed_numbers)

f1 = Rational(3, 4)
f2 = Rational(2, 9)
c1 = Rational(23, 55)
f3 = f1 - f2
f4 = f1 + f2
f5 = f2 * c1
f6 = f1 * f2

print(f3, f4, f5, f6)
print(Rational.processed_numbers)

# 19/36 35/36 46/495 1/6
