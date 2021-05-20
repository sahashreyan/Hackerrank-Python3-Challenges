#https://www.hackerrank.com/challenges/validating-credit-card-number 
def check(string):
    str_list = []
    if(len(string) == 16):
        if(string.isdigit() == bool(1)):
            return 0
        else:
            return 1
    elif(len(string) != 19):
        return 1
    else:
        str_list = list(string)
        if(str_list[4] == str_list[9] == str_list[14] == '-'):
            string = string[0:4]+string[5:9]+string[10:14]+string[15:19]
            if(string.isdigit() == bool(1)):
                return 0
            else:
                return 1
        else:
            return 1 
        
def check1(string):
    str_list1 = []
    if((len(string) != 19) and (len(string) !=16)):
        return 1
    elif(len(string) == 16):
        str_list1 = list(string)
        if((str_list1[0] == '4') or (str_list1[0] == '5') or (str_list1[0] == '6')):
            return 0
        else:
            return 1
    else:
        string = string[0:4]+string[5:9]+string[10:14]+string[15:19]
        str_list1 = list(string)
        if((str_list1[0] == '4') or (str_list1[0] == '5') or (str_list1[0] == '6')):
            return 0
        else:
            return 1
        
def check2(string):
    str_list2 = []
    j = 0
    h = 0
    if((len(string) != 16) and (len(string) != 19)):
        j += 1
        return 1
    elif(len(string) == 19):
        string = string[0:4]+string[5:9]+string[10:14]+string[15:19]
        str_list2 = list(string)
    else:
        str_list2 = list(string)
    
    if(j == 0):
        for i in range(13):
            if(str_list2[i] == str_list2[i+1] == str_list2[i+2] == str_list2[i+3]):
                h += 1
                
    if(h == 0 and j == 0):
        return 0
    elif(h != 0 and j == 0):
        return 1
    
n = int(input()) 
validity = []
for i in range(n):
    card = input()
    if(check(card) !=0):
        validity.append("Invalid")
        #print('Check output: ', check(card))
    elif(check1(card) != 0):
        validity.append("Invalid")
        #print('Check1 output: ', check1(card))
    elif(check2(card) != 0):
        validity.append("Invalid")
        #print('Check2 output:', check2(card))
    else:
        validity.append("Valid")
        
for i in range(n):
    print(validity[i])


    
   
