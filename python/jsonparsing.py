import urllib.request, json
import csv
with urllib.request.urlopen("http://database.jturnerresearch.com/company/addeddeleted/") as url:
    data = json.loads(url.read().decode())

for key in data.items() :
    lst = data['added']
print(lst[0])
count = 0
with open('example4.csv', 'w+') as csvfile:
    fieldnames = ['jtc_id','is_client','name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in lst:


      writer.writerow(lst[count])
      count=count+1

print("Writing complete")
