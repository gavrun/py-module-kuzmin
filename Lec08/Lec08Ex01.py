import time

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
name_list = []

start_time = time.time()

# O(n^2)
for line in open(imdb_file, encoding="utf-8"): # O(n)
    words = line.strip().split('|')
    name = words[0].strip()
    if not name in name_list: # O(n), where n ~ len(name_list)
        name_list.append(name)
        if len(name_list) % 1000 == 0:
            end_time = time.time()
            print('After {} added, the last 1000 took {:.2f} seconds'.format(len(name_list), end_time-start_time))
            start_time = end_time
print(name_list)
