#
#
# change
#
#

def powersOf2(n):
    pow = 1
    print("fun, out: ",pow)
    for i in range(n):
        if i==3:
            yield pow
            return pow
        else:
            yield pow
        print("fun, in: ",pow,"i: ",i)
        pow *= 2

for v in powersOf2(8):
    print(v)
