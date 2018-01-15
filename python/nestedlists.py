import itertools
def takeSecond(elem):
    return elem[1]
if __name__ == '__main__':
    lll=[]
    n = int(input())
    lst2=[]
    lst = [[] for _ in range(n)]
    #print(lst)
    for i in range(0,n):
        name = input()
        score = float(input())

        lst[i].append(name)
        lst[i].append(score)

    lst.sort(key=takeSecond)
    #lst.remove(key=takeSecond)
    #for i in range(0,len(lst)):
        #lists=lst[len(lst)]
        #listss=lst[len(lst)-1]


    merged = list(itertools.chain.from_iterable(lst))
    #for i in range(0,len(merged)):
    #    if merged[1]==merged[3]:
    #        merged.pop()
    #        merged.pop()

    if merged[1]==merged[3]==merged[5]:
        print(merged[6])
    else:
        if merged[3]==merged[5]:
            lll.append(merged[2])
            lll.append(merged[4])
            lll=sorted(lll)
            print(lll[0])
            print(lll[1])

        else:
            if merged[1]==merged[3] and merged[5]==merged[7]:
                print(merged[6])
                print(merged[4])

            else:
                print(merged[2])



    
