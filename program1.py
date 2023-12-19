#converting Decimal number to binary, octal and hexadecimal.
def decimal_to_binary(decimal_num):
    binary_result = ''
    while decimal_num > 0:
        binary_result = str(decimal_num % 2) + binary_result
        decimal_num //= 2
    return binary_result

def decimal_to_octal(decimal_num):
    octal_result = ''
    while decimal_num > 0:
        octal_result = str(decimal_num % 8) + octal_result
        decimal_num //= 8
    return octal_result

def decimal_to_hexadecimal(decimal_num):
    hexadecimal_result = ''
    while decimal_num > 0:
        remainder = decimal_num % 16
        if remainder < 10:
            hexadecimal_result = str(remainder) + hexadecimal_result
        else:
            hexadecimal_result = chr(ord('A') + remainder - 10) + hexadecimal_result
        decimal_num //= 16
    return hexadecimal_result

# Example usage:
decimal_number = int(input("Enter a decimal number: "))

binary_result = decimal_to_binary(decimal_number)
octal_result = decimal_to_octal(decimal_number)
hexadecimal_result = decimal_to_hexadecimal(decimal_number)

print("Binary:", binary_result)
print("Octal:", octal_result)
print("Hexadecimal:", hexadecimal_result)
