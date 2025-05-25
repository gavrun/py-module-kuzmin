# sorting lists

numbers = [1,2,20,7,8,9,10,11,3,4,5,6,12,15]

numbers.sort()
print(numbers)

# sorting strings

text = "This is the sentence."

sorted_text1 = sorted(text)
print(sorted_text1)

sorted_text2 = sorted(text.split()) # capital T is before lower t in ASCI
print(sorted_text2)

sorted_text3 = sorted(text.split(), key=lambda x: x[1]) # second char
print(sorted_text3)

#

