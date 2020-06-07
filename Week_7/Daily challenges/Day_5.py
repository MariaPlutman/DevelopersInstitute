def reverseBits(num):
    bit = int('{:032b}'.format(num)[::-1], 2)
    binary = []
    n = int(bit)

    while n != 0:
        binary.append(n % 2)
        n = n//2
    binary.reverse()
    binary = ''.join(map(str, binary))
    return (f'Code in 32 bits is: {bit} and it\'s code in binary is {binary}')


print(reverseBits(1234))
