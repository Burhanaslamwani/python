if __name__ == '__main__':
    N = int(input())
    l = []
    lst_two = []
    for z in range(0,N):
        st=input()
        l.append(st)
        del st

    for i in range(0,N):
        s=str(l[0])
        l.pop(0)
        lst=s.split(" ")
        if lst[0]=="insert":
            lst_two.insert(int(lst[1]),lst[2])
        if lst[0]=="print":
            print(lst_two)
        if lst[0]=="remove":
            lst_two.remove(lst[1])
        if lst[0]=="append":
            lst_two.append(lst[1])
        if lst[0]=="sort":
            lst_two.sort()
        if lst[0]=="pop":
            lst_two.pop()
        if lst[0]=="reverse":
            lst_two.reverse()
