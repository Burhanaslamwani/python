if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(0,len(arr)):
        if arr[len(arr)-1]==arr[len(arr)-2]:
            arr.pop()


    print(arr[len(arr)-2])
