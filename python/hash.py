if __name__ == '__main__':
    integer_list = int(input())
    def ch(x):return int(x)
    integer_list = list(map(ch, input().split(" ")))
    print(integer_list)
    t=tuple(integer_list)
    print(hash(t))
