import struct

def write_binary_data(filename, data):
    with open(filename, 'wb') as file:
        for item in data:
            if isinstance(item, int):
                # Write a type marker (1 byte) followed by the integer
                file.write(b'i')
                file.write(struct.pack('i', item))
            elif isinstance(item, float):
                # Write a type marker (1 byte) followed by the float
                file.write(b'f')
                file.write(struct.pack('f', item))

def read_binary_data(filename):
    data = []
    with open(filename, 'rb') as file:
        while True:
            # Read the type marker
            type_marker = file.read(1)
            if not type_marker:  # End of file
                break
                
            # Read the value (4 bytes)
            value_bytes = file.read(4)
            if not value_bytes:  # Unexpected end of file
                break
                
            if type_marker == b'i':
                data.append(struct.unpack('i', value_bytes)[0])
            elif type_marker == b'f':
                data.append(struct.unpack('f', value_bytes)[0])
    
    return data

# Example usage
data_to_write = [10, 3.14, 25, 1.618, 100]
filename = "my_data_fixed.bin"
write_binary_data(filename, data_to_write)

read_data = read_binary_data(filename)
print("Original data:", data_to_write)
print("Read data:", read_data)

# Let's also verify with more complex data including consecutive integers and floats
complex_data = [10, 20, 3.14, 2.71, 100, 200, 1.618]
filename2 = "complex_data.bin"
write_binary_data(filename2, complex_data)

read_complex = read_binary_data(filename2)
print("\nComplex data:", complex_data)
print("Read complex data:", read_complex)
