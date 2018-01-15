def mutate_string(string, position, character):
    l = list(string)
    #l.insert(position , character)
    l[position]=character
    return print("".join(l))
string = input()
position = input().split(" ")
#print(position)
#character = input()
mutate_string(string, int(position[0]), position[1])
