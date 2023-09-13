stroka = str(input()).rstrip().lstrip()
c = 1
for i in range(len(stroka)):
    if stroka[i] == " ":
        c += 1
print(f"Колличество слов в строке : {c}")