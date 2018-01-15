def count_substring(string, sub_string):
    if len(string)<=200:
        v=0
        counter =0
        for i in range(0,len(string)):

            if i <= (len(string)+1)-len(sub_string):
                counter=0
                for x in range(0,len(sub_string)):
                    if string[i] == sub_string[x]:
                      counter = counter+1
                      print(counter)
                      if counter==len(sub_string):
                         v=v+1
                         counter=0


            #if string[i]==sub_string[0]:
             #i=i+1
             #if string[i]==sub_string[1]:
                #i=i+1
                #if string[i]==sub_string[2]:



    return print(v)

string = input()
sub_string = input()
count_substring(string, sub_string)
