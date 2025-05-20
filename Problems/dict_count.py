def count_chars(s):
    counts = {  }

    for char in s:
        counts.setdefault(char, 0)
        counts[char] += 1

    return len(counts.keys())

print(count_chars('hello_world!')) # 12
