def combine_lists(list1, list2):
    """
    Combines two lists of elements with position information.
    
    Args:
        list1: First list of elements with positions and values
        list2: Second list of elements with positions and values
        
    Returns:
        list: Combined and processed list
    """
    # Combine both lists
    combined = list1 + list2
    
    # Sort by left position
    combined.sort(key=lambda x: x['positions'][0])
    
    i = 0
    while i < len(combined) - 1:
        current = combined[i]
        next_item = combined[i + 1]
        
        # Calculate overlap
        current_left, current_right = current['positions']
        next_left, next_right = next_item['positions']
        
        # Calculate overlap percentage
        overlap = min(current_right, next_right) - max(current_left, next_left)
        current_length = current_right - current_left
        next_length = next_right - next_left
        
        # If more than half of either element is contained within the other
        if overlap > 0 and (overlap > current_length / 2 or overlap > next_length / 2):
            # Merge the two elements
            new_left = min(current_left, next_left)
            new_right = max(current_right, next_right)
            new_values = current['values'] + next_item['values']
            
            # Create new element
            combined[i] = {
                'positions': [new_left, new_right],
                'values': new_values
            }
            # Remove the next element
            combined.pop(i + 1)
        else:
            i += 1
    
    return combined

# Example usage
if __name__ == "__main__":
    # Test case 1: Overlapping elements
    list1 = [
        {'positions': [1, 5], 'values': ['A']},
        {'positions': [10, 15], 'values': ['B']}
    ]
    list2 = [
        {'positions': [3, 7], 'values': ['C']}
    ]
    
    print("Test Case 1:")
    print("List 1:", list1)
    print("List 2:", list2)
    print("Combined:", combine_lists(list1, list2))
    
    # Test case 2: Non-overlapping elements
    list3 = [
        {'positions': [1, 3], 'values': ['X']},
        {'positions': [7, 9], 'values': ['Y']}
    ]
    list4 = [
        {'positions': [4, 6], 'values': ['Z']}
    ]
    
    print("\nTest Case 2:")
    print("List 1:", list3)
    print("List 2:", list4)
    print("Combined:", combine_lists(list3, list4))
    
    # Test case 3: Nested elements
    list5 = [
        {'positions': [2, 8], 'values': ['P']},
        {'positions': [12, 18], 'values': ['Q']}
    ]
    list6 = [
        {'positions': [4, 6], 'values': ['R']},
        {'positions': [14, 16], 'values': ['S']}
    ]
    
    print("\nTest Case 3:")
    print("List 1:", list5)
    print("List 2:", list6)
    print("Combined:", combine_lists(list5, list6))
