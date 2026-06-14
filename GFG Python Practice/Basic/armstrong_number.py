# Armstrong Number
n = 153
s = str(n)
l = len(s)
sum_val = sum(int(i)**l for i in s)
print(n == sum_val)
