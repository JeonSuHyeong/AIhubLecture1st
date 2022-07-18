price = 1000 # 전역변수

def sale():
    price = 500 # 지역변수
    print(price)


print(price)
sale()
print(price)
