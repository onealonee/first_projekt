stroka = str(input()).lower().replace(" ","")
c = 0
for i in range(len(stroka)):
    if stroka[i] == stroka[-i-1]:
        c += 1
if c == len(stroka):
    print("Палиндром")
else:
    print("NO")