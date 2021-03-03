def cmmdc(a: int, b: int):
    """Get the lowest common denominator
    """
    a = abs(a)
    b = abs(b)
    if a > b:
        return cmmdc(a-b, a)
    elif a < b:
        return cmmdc(a, b-a)
    else:
        return a
