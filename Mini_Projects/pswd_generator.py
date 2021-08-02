import random
length = int(input("Enter the length of the password: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&"
p = "".join(random.sample(s,length))
print("Your password is: "+p)
