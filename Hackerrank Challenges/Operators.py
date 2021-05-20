#https://www.hackerrank.com/challenges/30-operators/problem
#!/bin/python3
import math
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

cost = float(meal_cost + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100))
print(round(cost))
