#program to convert binary,octal and hexadecimal to decimal number
def binary_to_decimal(binary_num):
    decimal_result = 0
    binary_num = str(binary_num)[::-1]
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            decimal_result += 2 ** i
    return decimal_result

def octal_to_decimal(octal_num):
    decimal_result = 0
    octal_num = str(octal_num)[::-1]
    for i in range(len(octal_num)):
        decimal_result += int(octal_num[i]) * 8 ** i
    return decimal_result

def hexadecimal_to_decimal(hexadecimal_num):
    decimal_result = 0
    hexadecimal_num = str(hexadecimal_num)[::-1]
    for i in range(len(hexadecimal_num)):
        if hexadecimal_num[i].isdigit():
            decimal_result += int(hexadecimal_num[i]) * 16 ** i
        else:
            decimal_result += (ord(hexadecimal_num[i].upper()) - ord('A') + 10) * 16 ** i
    return decimal_result

# Example usage:
binary_input = input("Enter a binary number: ")
octal_input = input("Enter an octal number: ")
hexadecimal_input = input("Enter a hexadecimal number: ")

decimal_from_binary = binary_to_decimal(binary_input)
decimal_from_octal = octal_to_decimal(octal_input)
decimal_from_hexadecimal = hexadecimal_to_decimal(hexadecimal_input)

print("Decimal from Binary:", decimal_from_binary)
print("Decimal from Octal:", decimal_from_octal)
print("Decimal from Hexadecimal:", decimal_from_hexadecimal)
