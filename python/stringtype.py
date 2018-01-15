if __name__ == '__main__':
    str = input()
    lst = list(str)
    x = "false"
    y = "false"
    z = "false"
    v = "false"
    for i in range(0,len(lst)):
        print(i)
        if lst[i].isalpha():
            x = "true"

        if lst[i].isdigit():
            y = "true"
        if lst[i].isupper():
            z = "true"
        if lst[i].islower():
            v = "true"

    if x=="true" or y== "true":
        print("true")
    else:
        print("false")
    if x=="true":
        print("true")
    else:
        print("false")
    if y=="true":
        print("true")
    else:
        print("false")
    if z=="true":
        print("true")
    else:
        print("false")
    if v=="true":
        print("true")
    else:
        print("false")
