#https://www.hackerrank.com/challenges/python-print/problem
if __name__ == '__main__':
    n = int(input())
    num = []
    for i in range(1, n+1):
        num.append(i)
        
    for i in range(n):
        print(num[i], end="")
        
