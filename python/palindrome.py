string = input()
list = []
list2 = []
for i in string:
	list.append(i)
#print(list)
#list2 = list
a = b = len(list)

print(list2,a)
for i in range(len(list)):
   list2.append(list[len(list)-1-i]);
if list == list2:
    print("palindrome")
print(list2)
