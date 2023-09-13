a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4/a*c
if D > 0:
    print((-b + D**(1/2))/2*a, (-b -D**(1/2))/2*a )
if D == 0:
    print(-(b/(2*a)))
else:
    print("Действительных корней - нет ")