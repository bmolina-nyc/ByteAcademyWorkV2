
def mcnugg(x):
    """This is what the function does
    input: x, a number (integer)
    output: mcnugget numbers up to x
    """
    mcnumbs=[0]
    i=1
    not_nug=[]
    while i<=x:
        if i-6 in mcnumbs or i-9 in mcnumbs or i-20 in mcnumbs:
            mcnumbs.append(i)
            i+=1
        else:
            i+=1

    for num in range(0,i):
        if num not in mcnumbs:
            not_nug.append(num)
    return not_nug

value = int(input('Choose a number: '))

print(mcnugg(value))

