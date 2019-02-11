

def towers_of_hanoi(n, initial_peg, aux_peg, final_peg):
    if n <= 0:
        pass
    else:
        for h in towers_of_hanoi(n-1, initial_peg, final_peg, aux_peg):
            yield h
        yield (initial_peg, aux_peg)
        for h in towers_of_hanoi(n-1, final_peg, aux_peg, initial_peg):
            yield h

print([h for h in towers_of_hanoi(3,1,2,3)])