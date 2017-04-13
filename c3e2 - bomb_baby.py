def answer(M, F):
    m = int(M)
    f = int(F)

    gen = 0

    while m != 1 or f != 1:
        if m == f or m < 1 or f < 1:
            break
        elif m > f:
            multiplier = m // f
            if f == 1:
                gen += multiplier - 1
                m -= (f * multiplier) - 1
            else:
                gen += multiplier
                m -= f * multiplier
        else:
            multiplier = f // m
            if m == 1:
                gen += multiplier - 1
                f -= (m * multiplier) - 1
            else:
                gen += multiplier
                f -= m * multiplier

    if m == 1 and f == 1:
        return gen
    else:
        return "impossible"


print str(answer(2, 1)) + ", answer: 1"
print str(answer(2, 4)) + ", answer: impossible"
print str(answer(4, 7)) + ", answer: 4"
print str(answer(16, 43)) + ", answer: 9"
print str(answer(-3, 1)) + ", answer: impossible"
print str(answer(10 ** 50, 47)) + ", answer: ???"
