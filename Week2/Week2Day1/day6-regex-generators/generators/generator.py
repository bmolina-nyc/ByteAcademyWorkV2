def squarerange(maxval):
    n = 1
    while n * n < maxval:
        yield n * n
        n = n + 1
