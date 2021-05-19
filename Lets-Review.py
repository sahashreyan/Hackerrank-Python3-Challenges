#https://www.hackerrank.com/challenges/30-review-loop/problem
n = int(input())
string_list = []
for i in range(n):
    s = input()
    string_list.append(s)
    
for i in range(n):
    s = str(string_list[i])
    print(s[::2],s[1::2])
    