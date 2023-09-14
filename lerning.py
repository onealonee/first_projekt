<<<<<<< HEAD
# объявление функции
def is_password_good(password):
    c = 0
    if len(password) > 8:
        for i in range(len(password)):
            if password[i].upper() == password[i]:
                c += 1
            elif password[i].lower() == password[i]:
                c += 1
            #elif i

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
=======
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
>>>>>>> 35168e959269e04a1815f23df712f5977e3979b2
