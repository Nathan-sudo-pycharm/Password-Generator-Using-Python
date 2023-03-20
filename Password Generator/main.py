import random
passlen=int(input("enter the length of the password"))
s="abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*"
p="".join(random.sample(s,passlen))
print(p)