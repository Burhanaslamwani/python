num = []
for i in range(10):
    num.append(input('Enter the %s number: '))
num1 = []
#print (num)
for i in range(len(num)):
    if int(num[i])<11:
        num1.append(num[i])
print (num1)
