a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(0,len(b)):
    for x in range(0,len(a)):
        if b[i] == a[x]:
            print (b[i])

