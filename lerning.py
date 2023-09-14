# объявление функции
def is_password_good(password):
    c = 0
    if len(password) > 8:
        for i in range(len(password)):
            if password[i].upper() == password[i]:
                c += 1
            elif password[i].lower() == password[i]:
                c += 1
            elif i 

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))