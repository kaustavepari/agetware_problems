def caesar_cipher(message, shift, mode='encode'):
    """
    Encodes or decodes a message using Caesar Cipher.
    
    Args:
        message (str): The message to encode/decode
        shift (int): Number of positions to shift
        mode (str): 'encode' or 'decode'
        
    Returns:
        str: The encoded/decoded message
    """
    result = []
    shift = -shift if mode == 'decode' else shift
    
    for char in message:
        if char.isalpha():
            # Determine the base (A for uppercase, a for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Calculate the new position with wrap-around
            new_pos = (ord(char) - base + shift) % 26
            result.append(chr(base + new_pos))
        else:
            # Keep non-alphabetic characters as is
            result.append(char)
    
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    # Test encoding
    message = "Hello, World!"
    shift = 3
    encoded = caesar_cipher(message, shift)
    print(f"Original: {message}")
    print(f"Encoded: {encoded}")
    
    # Test decoding
    decoded = caesar_cipher(encoded, shift, 'decode')
    print(f"Decoded: {decoded}")
