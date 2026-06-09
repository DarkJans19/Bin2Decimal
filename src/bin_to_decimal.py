def convert_binary_to_decimal(binary):
    if len(binary) > 8:
        raise ValueError("You can only convert 8 binary length")
    
    for i in range(len(binary)):
        if binary[i] != '1' and binary[i] != '0':
            raise ValueError("The binary number can only have 1 or 0")

    result = 0

    for bit in binary:
        print(result)
        result = result * 2 + int(bit)

    return result


if __name__ == "__main__":
    user_input = input("Introduce the binary number you want convert: ")
    try:
        decimal_result = convert_binary_to_decimal(user_input)
        print(f"Result: {decimal_result}")
    except ValueError as e:
        print(f"Error: {e}")



