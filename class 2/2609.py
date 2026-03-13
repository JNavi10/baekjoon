i1, i2 = map(int, input().split())


# int1 > int2
def gcd(int1, int2):
    if int1 % int2 == 0:
        return int2
    else:
        return gcd(int2, int1%int2)
    
if i1 > i2:
    gcd_int = gcd(i1, i2)
else:
    gcd_int = gcd(i2, i1)

print(gcd_int)
print(i1*i2//gcd_int)