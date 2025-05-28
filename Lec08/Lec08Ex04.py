phone_book = {}
lu_by_phone = {}
while True:
    name = input('Enter name => ')
    if name == '':
        break
    phone = input('Enter phone number => ')
    if not name in phone_book:
        phone_book[name] = []
    phone_book[name].append(phone)
    if not phone in lu_by_phone:
        lu_by_phone[phone] = []
    lu_by_phone[phone].append(name)
print(phone_book)
print('Kostya' in phone_book)
print(phone_book['Kostya'])
print(len(phone_book['Kostya']))
print(phone_book['Kostya'][1])
print(lu_by_phone['123456'])
