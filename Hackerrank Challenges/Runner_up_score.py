#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
import math
n = int(input())
score = input()
score_list = score.split()
for i in range(n):
    score_list[i] = int(score_list[i])
    
score_list.sort(reverse=True)
high_count = score_list.count(score_list[0])
print(score_list[high_count])
