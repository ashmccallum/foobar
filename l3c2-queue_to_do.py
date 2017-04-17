from operator import xor

def answer(start, length):
    # your code here

    workers = []

    for i in xrange(length, 0, -1):
        # row = xrange(start, start + i, 1)

        # check starting number, even makes it easier
        if start % 2 == 0:
            # if number of even-odd pairs is even, they cancel each other out, otherwise they return 1
            if (i / 2) % 2 == 0:
                workers.append(0)
            else:
                workers.append(1)




        start += length

        # csArray.extend(row)
    checksum = reduce(xor, workers)

    return checksum


print "output: " + str(answer(0,3)) + ", answer: 2"
print "output: " + str(answer(17,4)) + ", answer: 14"
# print "output: " + str(answer(17,40)) + ", answer: ??"
