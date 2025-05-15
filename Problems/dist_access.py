def access_entry(d, item):
    for key in d:
        if key.lower() == item.lower():
            return d[key]
    return None

dict = { 'name': "Bob", 'Name': "Dick" }

print(access_entry(dict, "NAME"))
print(access_entry(dict, "name"))
