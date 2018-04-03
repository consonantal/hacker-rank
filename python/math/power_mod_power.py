a = int(raw_input())
b = int(raw_input())
m = int(raw_input())

if a <= 10 and a >= 1 and b <= 10 and b >= 1 and m <= 1000 and m >= 2:
    print pow(a, b)
    print pow(a, b, m)
else:
    print ''

