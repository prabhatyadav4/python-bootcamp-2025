def hyphen_to_space(text):
    """
    Converts hyphenated text to space-separated text with a leading space.
    
    Args:
        text (str): The hyphenated text to convert
        
    Returns:
        str: The converted text with spaces instead of hyphens and a leading space
    """
    # Replace hyphens with spaces
    space_separated = text.replace('-', ' ')
    
    # Add a leading space if it doesn't already have one
    if not space_separated.startswith(' '):
        space_separated = ' ' + space_separated
        
    return space_separated

# Example usage
if __name__ == "__main__":
    original_text = "Hey-I-am-good."
    converted_text = hyphen_to_space(original_text)
    
    print(f"Original: {original_text}")
    print(f"Converted: {converted_text}")