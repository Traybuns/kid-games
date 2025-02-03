def caesar_cipher(text, shift, direction):
    result = ""
    
    if direction == "decode":
        shift = -shift  # Reverse shift for decoding
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            result += char  # Keep spaces and punctuation unchanged

    return result


# Get user input
direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))  # User chooses shift

# Process the message
output = caesar_cipher(message, shift, direction)
print(f"Result: {output}")
