# STRUCT module allows you to save and restore packaged binary data
import struct
# Baytes packaging
dat1 = struct.pack("hhl", 1, 2, 3) # the first and second numbers are interpreted as the type of Short Int, and the third, as Long Int.
print(dat1) #B'\x01\x00\x02\x00\x03\x00\x00\x00'

# object size Dat1
size = struct.calcsize('hhl') #Size =8
print('size = ', size)

# unpacking byte in a motorcade of values ​​in a given format:
tup1 = struct.unpack("hhl", dat1)
print(tup1)

F = open('data.bin', 'wb') # Open a file for recording in binary mode

data = struct.pack("<2h", 7,11) # Create a package of binary data - Little -Endian (<) The order from the younger byte to the senior and h is repeated twice
print(data)

F.write(data) # Write a bait line
F.close()

# extracting values, converting them into ordinary objects

F = open('data.bin', 'rb')
data = F.read() # Get packaged binary data
print(data)

values = struct.unpack('<2h', data) # Transform into objects
print(values)

# Work with lines

# For lines, the code “S” must indicate the number of bytes - the length of the line, otherwise 1 byte will be considered:
print(struct.pack("ss", b"abc", b"XYZW"))  # did not indicate the length - lost bytes - b'AX '
print(struct.pack("3s4s", b"abc", b"XYZW")) #B'abcXyzw'

#10S-one 10-sMALL line, and 10C-10 separate characters:
print(struct.unpack('10c', b'abracadabr')) # (b'a',B'b',B'r',B'a',B'c',B'a',B'd',B'a',B'b',B'r')
print(struct.unpack('10s', b'abracadabr')) # (b'abracadabr ',)

# Gaps are ignored when reading a line and are needed for the convenience of reading code by a programmer:
print(struct.pack('>6sh?', b'python', 65, True)) #B'python\x00A\x01'
print(struct.pack('> 6s h ?', b'python', 65, True))  # too, but with gaps b'python \ x00a \ x01 '
print(struct.unpack('> 6s h ?', b'python\x00A\x01')) # (b'python',65,True)


# It is convenient to unpack bytes directly in the named trips:
from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
record = b'raymond   \x32\x12\x08\x01\x08'
print(Student._make(struct.unpack('<10sHHb', record)))
#Student(name=b'raymond ',Serialnum=4658,School=264,Gradelevel=8)






