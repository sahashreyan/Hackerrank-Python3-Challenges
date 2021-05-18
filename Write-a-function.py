#https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = False
    not_leap = True
    if((year % 4 != 0)):
        return leap
    if((year % 4 == 0)):
        if((year % 100 !=0)):
            return not_leap
        elif(year % 400 == 0):
            return not_leap
        else:
            return  leap

#Only the leap year checking function is written so you may add an input command to make it interactive!!