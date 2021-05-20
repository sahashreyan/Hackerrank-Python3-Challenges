#https://www.hackerrank.com/challenges/validating-the-phone-number/problem
n = int(input())
def check1(string):
    str_list = []
    str_list = list(string)
    if(int(str_list[0]) < 7):
        return 0
    else:
        return 1
    
def check(string):
    if(len(string) == 10):
        return 1
    else:
        return 0
    
def check2(string):
    if(str(string).isdigit() == True):
        return 1
    else:
        return 0
validity = []   
for i in range(n):
    num = str(input())
    if(check2(num) != 1):
        validity.append('NO')
    elif(check1(num) != 1):
        validity.append('NO')
    elif(check(num) != 1):
        validity.append('NO')
    else:
        validity.append('YES')
        
for i in range(n):
    print(validity[i])
    
    
