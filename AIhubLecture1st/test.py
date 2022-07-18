import numpy as np
import pandas as pd
import random as rd

answer = rd.randint(1,11)
print(answer)
print("숫자맞추기 게임\n")

for i in range(4,1,-1):
    num = int(input("숫자를 입력하세요 : "))
    if (answer == num):
        print("정답\n")
        break
    elif (answer > num):
        print(f"틀렸습니다. {num}보다 큰 수 입니다. {i-2}번의 기회가 남았습니다.")
    else:
        print(f"틀렸습니다. {num}보다 작은 수 입니다. {i-2}번의 기회가 남았습니다.")
