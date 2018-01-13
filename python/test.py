import sys

def simpleArraySum(w,z):
    x = 0
    for i in range(0,w):
     x=x+int(z[i])
    return x
w = int(input())
n = input()
z = list(n.split())
#print(n)
#z = list(n)

#ar = list(map(int, input().strip().split(' ')))
#x = join(ar)
#print(z)
result = simpleArraySum(w,z)
print(result)
