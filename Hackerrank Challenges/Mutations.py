#https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    result = string[:position] + character + string[position+1:]
    return result 

