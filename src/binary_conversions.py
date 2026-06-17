def convert_binary_to_decimal(binary):
    for i in range(len(binary)):
        if binary[i] != '1' and binary[i] != '0':
            raise ValueError("The binary number can only have 1 or 0")

    result = 0

    for bit in binary:
        print(result)
        result = result * 2 + int(bit)

    return result

def convert_decimal_to_binary(decimal):
    if decimal == "0":
        return "0"
    try:
        decimal = int(decimal)
    except:
        raise ValueError("The value entered must be a number") 
    binary = ""
    while decimal > 0:
        bin = decimal % 2
        decimal //= 2 
        binary = str(bin) + binary
    return binary