#import binascii
number = input("Enter a number: ")

string = bin(int(number))
output = '0b'

for c in string[2:]:
    print(c)
    output += '0' if (c == '1') else '1'

print(string)
print(int(output, 2))
