num = int(input())
n = str(input())
l = n.split()
for i in range(len(l)):
    l[i] = int(l[i])
    
l.reverse()
for  i in range(len(l)):
    print(l[i], end=" ")
    
    