def format_indian_currency(number):
    """
    Formats a number into Indian currency format.
    
    Args:
        number (float): The number to format
        
    Returns:
        str: Formatted Indian currency string
    """
    # Handle negative numbers
    sign = '-' if number < 0 else ''
    num = abs(number)
    
    # Split into integer and decimal parts
    integer_part = int(num)
    decimal_part = num - integer_part
    
    # Convert integer part to string and reverse for easier processing
    s = str(integer_part)[::-1]
    
    # Add commas according to Indian numbering system
    parts = []
    # First 3 digits (hundreds, tens, units)
    if len(s) > 3:
        parts.append(s[:3][::-1])
        s = s[3:]
    else:
        parts.append(s[::-1])
        s = ''
    
    # Process remaining digits in pairs
    while len(s) > 0:
        if len(s) >= 2:
            parts.append(s[:2][::-1])
            s = s[2:]
        else:
            parts.append(s[0])
            s = ''
    
    # Join with commas and reverse back
    formatted_int = ','.join(reversed(parts))
    
    # Handle decimal part if exists
    if decimal_part > 0:
        # Format with up to 4 decimal places and remove trailing zeros
        decimal_str = f"{decimal_part:.4f}".rstrip('0').rstrip('.')
        # Remove the leading '0' from decimal part
        if decimal_str.startswith('0.'):
            decimal_str = decimal_str[1:]
        return f"{sign}{formatted_int}{decimal_str}"
    return f"{sign}{formatted_int}"

# Example usage
if __name__ == "__main__":
    # Test cases
    test_numbers = [
        123456.7891,     # 1,23,456.7891
        123456789,       # 12,34,56,789
        12345.67,        # 12,345.67
        10000000,        # 1,00,00,000
        -1234567.89,     # -12,34,567.89
        0.1234,          # 0.1234
        123,             # 123
        1234,            # 1,234
        12345,           # 12,345
    ]
    
    for num in test_numbers:
        formatted = format_indian_currency(num)
        print(f"{num:15,.4f} -> {formatted}")
