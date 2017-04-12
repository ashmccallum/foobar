def answer(M, F):
    m = int(M)
    f = int(F)

    gen = 0

    if (m != 1 or f != 1) and (m % f == 0) or (f % m == 0) or (m % 2 == 0 and f % 2 == 0) and (m < 1 and f < 1):
        return "impossible"
    elif m >= 10 ** 50 and f >= 10 * 50:
        return "impossible"

    while m != f:
        if m < 1 and f < 1:
            break
        elif m > f:
            m -= f
            gen += 1
        else:
            f -= m
            gen += 1

    if m == 1 or f == 1:
        return gen
    # elif m == 1:
    #     gen += f - 1
    #     return gen
    # elif f == 1:
    #     gen += m - 1
    #     return gen
    else:
        return "impossible"


# print answer(2,1)
# print answer(2,4)
# print answer(4,7)
# print answer(16,43)
print answer(-3,1)
print answer(10**10,47)
