import struct

# Writing data to a binary file
def write_binary_data(filename, data):
    with open(filename, 'wb') as file:
        for item in data:
            if isinstance(item, int):
                file.write(struct.pack('i', item))  # 'i' for integer
            elif isinstance(item, float):
                file.write(struct.pack('f', item))  # 'f' for float

# Reading data from a binary file
def read_binary_data(filename):
    data = []
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(4) # Read 4 bytes
            if not chunk:
                break
            try:
                data.append(struct.unpack('i', chunk)[0])
            except struct.error:
              file.seek(-4,1)
              chunk = file.read(4)
              if not chunk:
                break
              data.append(struct.unpack('f',chunk)[0])
    return data

# Example usage
data_to_write = [10, 3.14, 25, 1.618, 100]
filename = 'my_data.bin'
write_binary_data(filename, data_to_write)

read_data = read_binary_data(filename)
print(read_data)
