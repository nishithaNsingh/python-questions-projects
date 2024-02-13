a = int(input())
b = int(input())
x = max(a,b)
y = min(a,b)
reminder = 1
while (y != 0): 
            remainder = x % y
            x = y
            y = remainder
hcf = x 
lcm = (a * b) / hcf          
print(f"HCF of {a} and {b}: {hcf}")
print(f"LCM of {a} and {b}: {lcm}")