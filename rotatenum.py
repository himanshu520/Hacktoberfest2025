# Function to rotate number
def rotate_number(num, k):
    num_str = str(num)
    k = k % len(num_str) 
    
    
    rotated = num_str[-k:] + num_str[:-k]
    
    return int(rotated)


number = int(input("Enter a number: "))
k = int(input("Enter how many times to rotate: "))

rotated_number = rotate_number(number, k)
print(f"Rotated number: {rotated_number}")
