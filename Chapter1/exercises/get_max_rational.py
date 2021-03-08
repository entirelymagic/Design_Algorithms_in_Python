from Chapter1.def_rational_numbers import Rational as R


def maximum(*args):
    return max(args)


f1 = R(1, 8)
f2 = R(3, 5)
f3 = R(2, 7)
f4 = R(1, 5)
f5 = R(3, 9)
f6 = R(4, 11)

l1 = [f1, f2, f3, f4, f5, f6]
l2 = [
    f1.decimal_form,
    f2.decimal_form,
    f3.decimal_form,
    f4.decimal_form,
    f5.decimal_form,
    f6.decimal_form,
]

print(maximum(*l1))

