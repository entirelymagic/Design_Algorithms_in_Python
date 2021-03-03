from Chapter1.def_rational_numbers import Rational


"""Operations performed with rational numbers"""


f1 = Rational(3, 4)
f2 = Rational(2, 9)
r1 = f1 * f2

print(r1)
print(Rational.processed_numbers)

f1 = Rational(1, 8)
f2 = Rational(1, 4)

r2 = f1 / f2
r3 = f2 / f1
print(r2, r3)
