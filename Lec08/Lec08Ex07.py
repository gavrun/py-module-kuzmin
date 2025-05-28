import time

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
name_list = []

start_time = time.time()

# O(n) + O(n * log n) + O(n) = O(n * log n)
for line in open(imdb_file, encoding="utf-8"): # O(n)
    words = line.strip().split('|')
    name = words[0].strip()
    name_list.append(name)
name_list.sort() # O(n * log n)
result = []
for i in range(1, len(name_list)):  # O(n)
    if name_list[i - 1] != name_list[i]:
        result.append(name_list[i])
end_time = time.time()
print('Total time required {:2f} seconds'.format(end_time-start_time))
                                                 
#print(result)
