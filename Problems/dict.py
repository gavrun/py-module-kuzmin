# Hanging indent

dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }

# 

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
          
for english, french in dictionary.items():
    print(english, "->", french)

for french in dictionary.values():
    print(french)

#

dictionary['cat'] = 'minou'
print(dictionary)

dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"duck": "canard"})
print(dictionary)

del dictionary['dog']
print(dictionary)

dictionary.popitem()
print(dictionary)
