def answer(M, F):
    mBombs = 1
    fBombs = 1
    gens = 0

    if M > 1000 or F > 1000:
        return "impossible"

    # take the largest from M & F, 1st generation to aim towards that
    while mBombs < M or fBombs < F:
        if (int(M) - mBombs) >= (int(F) - fBombs):
            mBombs = mBombs + fBombs
            gens += 1
        else:
            fBombs = fBombs + mBombs
            gens += 1

        print "M: " + str(mBombs) + ", F: " + str(fBombs)

    return str(gens)

print answer(2,1)
print answer(4,7)