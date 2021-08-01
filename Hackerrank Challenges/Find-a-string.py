#https://www.hackerrank.com/challenges/find-a-string
def count_substring(string, sub_string):
    str_list = list(string)
    sub_list = list(sub_string)
    l = len(sub_string)
    c = 0
    for i in range(len(string) - l +1):
        if(str_list[i] == sub_list[0]):
            if(sub_list == str_list[i : (i+l)]):
                c += 1
    return c



