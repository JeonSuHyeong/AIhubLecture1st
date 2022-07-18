a = input("수식 : ")
b = a.split(" ")

def calcul(a,b, char):
    if(char == "+"):
        return a+b
    elif(char == "-"):
        return a-b
    elif(char == "*"):
        return a*b
    elif(char == "/"):
        return a/b
    else:
        return 0
answer = calcul(int(b[0]),int(b[2]),b[1])

print(f"{b[0]} {b[1]} {b[2]} = {answer}")



"""
a = int(input("숫자 1 : "))
char = input("수식 : ")
b = int(input("숫자 2 : "))

def calcul(a,b, char):
    if(char == "+"):
        return a+b
    elif(char == "-"):
        return a-b
    elif(char == "*"):
        return a*b
    elif(char == "/"):
        return a/b
    else:
        return 0
answer = calcul(a,b,char)
print(f"{a}{char}{b} = {answer}")
"""