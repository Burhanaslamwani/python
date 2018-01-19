import urllib.request, json
with urllib.request.urlopen("http://database.jturnerresearch.com/company/addeddeleted/") as url:
    data = json.loads(url.read().decode())
    print(data)
for key, value in data.items() :
    print(key)
