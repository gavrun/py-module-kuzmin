import time

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
names = set()

start_time = time.time()

# O(n)
for line in open(imdb_file, encoding="utf-8"): # O(n)
    words = line.strip().split('|')
    name = words[0].strip()
    if not name in names: # O(1)
        names.add(name)
        # if len(names) % 1000 == 0:
        #     end_time = time.time()
        #     print('After {} added, the last 1000 took {:.2f} seconds'.format(len(names), end_time-start_time))
        #     start_time = end_time
#print(names)
end_time = time.time()
print("Solution took {:.2f} seconds".format(end_time-start_time))
