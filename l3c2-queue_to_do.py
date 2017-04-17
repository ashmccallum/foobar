from operator import xor

def answer(start, length):
    # your code here

    workers = []

    for i in xrange(length, 0, -1):
        # row = xrange(start, start + i, 1)

        # check starting number, even makes it easier
        if start % 2 == 0:
            if i % 2 == 0:
                # if number of even-odd pairs is even, they cancel each other out, otherwise they return 1
                if (i / 2) % 2 == 0:
                    # even start, even number of items, even number of even-odd pairs
                    workers.append(0)
                else:
                    # even start, even number of items, odd number of even-odd pairs
                    workers.append(1)
            else:
                if ((i - 1) / 2) % 2 == 0:
                    if i == 1:
                        workers.append(start)
                    else:
                        # even start, odd number of items, even number of even-odd pairs
                        workers.extend([0, start + i])
                else:
                    # even start, odd number of items, odd number of even-odd pairs
                    workers.extend([1, start + (i - 1)])
        else:
            if i % 2 == 0:
                if (i / 2) % 2 == 0:
                    # odd start, even number of items, even number of even-odd pairs
                    workers.extend([start, 0, start + i])
                else:
                    if (i / 2) == 1:
                        workers.extend([start, start + 1])
                    else:
                        # odd start, even number of items, odd number of even-odd pairs
                        workers.extend([start, 1, start + i])
            else:
                if ((i - 1) / 2) % 2 == 0:
                    # odd start, odd number of items, even number of even-odd pairs
                    workers.extend([start, 0])
                else:
                    # odd start, odd number of items, odd number of even-odd pairs
                    workers.extend([start, 1])

        start += length

    return reduce(xor, workers)


print "output: " + str(answer(0,3)) + ", answer: 2"
print "output: " + str(answer(17,4)) + ", answer: 14"
# print "output: " + str(answer(17,40)) + ", answer: ??"
