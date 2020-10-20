def XOR_bits(): # xor c point bits operation
    xor = without_last_bit[length_of_initial_state - 1]
    for point in range(len(XOR_c_points) - 1):
        xor = without_last_bit[XOR_c_points[point]] ^ xor
    new_bit.append(xor)
    return new_bit

global XOR_c_points
degree = input("Enter degree of LFSR  (ie.10):") #get LFSR degree
intial_state = list(input("Enter intial state in bits i.e 1110:")) #get intial state bits
intial_state = [int(bit) for bit in intial_state]
XOR_c_points = input("Enter XOR block positions (i.e. 0,3,4) :").split(',') #get postions of c values being 1
XOR_c_points = [int(point) for point in XOR_c_points]
no_of_cycle = input("Enter length or cycle of output bits i.e. 20:") #get number of output bits to display

intial_state.insert(0, intial_state[len(intial_state) - 1])
intial_state.pop()
without_last_bit = intial_state
length_of_initial_state = len(intial_state)
new_bit = []
output_bits = [0]
for value in range(int(no_of_cycle)): #get output bits for required cycle
    output_bits.insert(0, without_last_bit[length_of_initial_state - 1])
    XOR_bits()
    for value in range(length_of_initial_state - 1):
        new_bit.append(without_last_bit[value])

    without_last_bit = new_bit
    new_bit = []

output_bits.pop()
output_bits.reverse() #reverse bit order
output_data = ''.join(str(bit) for bit in output_bits)
print("Your output ",no_of_cycle, " bits is:",output_data)
