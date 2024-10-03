def decrypt_eligma_code(encoded_str):
    # Step 1: Sum the digits in the input string
    digit_sum = sum(int(char) for char in encoded_str if char.isdigit())
    
    # Step 2: Shift alphabet characters by digit_sum
    decrypted_message = ""
    for char in encoded_str:
        if char.isalpha():
            # Calculate the new character after shifting
            new_char = chr((ord(char) - ord('a') + digit_sum) % 26 + ord('a')) if char.islower() else \
                       chr((ord(char) - ord('A') + digit_sum) % 26 + ord('A'))
            decrypted_message += new_char
            
    return decrypted_message

# Example usage
input_str = "M13b3yni"
output = decrypt_eligma_code(input_str)
print(output)  # Output: tifup

