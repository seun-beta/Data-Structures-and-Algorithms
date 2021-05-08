def smallest_positive(in_list):
    
    smallest_pos = None
    for i in in_list:
        
        if i > 0:
            
            if smallest_pos == None or i < smallest_pos:
                smallest_pos = i
            else:
                smallest_pos = smallest_pos
    return smallest_pos


print(smallest_positive([-3.53, -56.3, 11.17, -25.21, 96.21, -44.62, 94.95, 65.85, 26.79, -88.16]))
