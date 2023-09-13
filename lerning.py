def is_prime(num):
    c = 0
    x = num
    while num != 10000:
        for i in range(1,num +1):
            if num % i == 0:
                c += 1
        if c == 2 and x != num:
            x = num
            num = 10000
            return(x)
        c = 0
        num += 1
n = int(input())
print(is_prime(n))