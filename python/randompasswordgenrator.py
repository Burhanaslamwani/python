import  random
pas =[]
for i in range(0,6):
 pas.append(random.choice( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k ', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] ))
#print(pas)
for i in range(0,3):
  pas.append(random.choice(["0","1","2","3","4","5","6","7","8","9"]))
for i in range(0,3):
  pas.append(random.choice(["!","@","#","$"]))
#print(pas)
str=''.join(pas) 
print(str)
