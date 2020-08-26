a=1071
b=1028

multi= a*b

if a<b:
    a,b = b,a
while a!=b:
    a,b = b,a-b
    print(a,b)
gcd = a
lcd = multi/gcd
print(lcd)
