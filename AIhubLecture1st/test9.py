import time

now = time.localtime()
print("%d년 %d월 %d일" %(now.tm_year,now.tm_mon, now.tm_mday))