import time
sec = 0
print("Введите время")
local_time = str(input()).split()
sec = int(local_time[0])*60*60+int(local_time[1])*60+int(local_time[2])
time.sleep(sec)
print("Время вышло")