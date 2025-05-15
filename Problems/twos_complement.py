def to_twos_complement(n, bits=8):
    # Step 1: If n is positive or zero, convert to binary.
    if n >= 0:
        return bin(n)[2:].zfill(bits)
    # Step 2: If n is negative, calculate the two's complement.
    else:
        # Find the binary representation of the positive version of n.
        positive_bin = bin((1 << bits) + n)[2:]
        return positive_bin

# Example: Convert 5 and -5 to two's complement with 8 bits.
positive_num = 5
negative_num = -5

# Convert to two's complement
positive_bin = to_twos_complement(positive_num)
negative_bin = to_twos_complement(negative_num)

print(f"Positive number {positive_num} in binary (8-bit): {positive_bin}")
print(f"Negative number {negative_num} in two's complement (8-bit): {negative_bin}")
