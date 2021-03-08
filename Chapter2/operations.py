def putere(r, n):

    putere = 1
    while n > 0:
        if n % 2 == 1:
            putere *= r
            n -= 1
        r *= r
        n /= 2
    return putere


print(putere(3, 15))
