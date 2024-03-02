def binary_to_int(arg):
    return [f'{bin(i)} = {int(i)}' for i in arg]


def int_to_binary(arg):
    return [f'{i} = {bin(i)}' for i in arg]


int_list = [15, 27, 73, 105]
bin_list = [0b111, 0b10101, 0b11011, 0b110101011]
print(int_to_binary(int_list))
print(binary_to_int(bin_list))

'''/usr/bin/python3.10 /home/user/PycharmProjects/py95/homeworks/1/bynary_number_system.py 
['15 = 0b1111', '27 = 0b11011', '73 = 0b1001001', '105 = 0b1101001']
['0b111 = 7', '0b10101 = 21', '0b11011 = 27', '0b110101011 = 427']

Process finished with exit code 0'''
