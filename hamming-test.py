def calculate_parity(bits, parity_bits):
    p = [0] * parity_bits
    p[0] = bits[0] ^ bits[1] ^ bits[3]
    p[1] = bits[0] ^ bits[2] ^ bits[3]
    p[2] = bits[1] ^ bits[2] ^ bits[3]
    return p

def create_hamming(bits, p):
    hamming = [0] * 7
    hamming[2] = bits[0]
    hamming[4] = bits[1]
    hamming[5] = bits[2]
    hamming[6] = bits[3]
    hamming[0] = p[0]
    hamming[1] = p[1]
    hamming[3] = p[2]
    return hamming

data = [1, 1, 0, 1]  # Input data bits
parity_bits = 3

p = calculate_parity(data, parity_bits)
hamming = create_hamming(data, p)

print("Hamming code: ", end="")
for bit in hamming:
    print(bit, end="")