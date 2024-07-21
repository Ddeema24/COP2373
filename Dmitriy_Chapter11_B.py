import math

def calculate_hypotenuse(angle_degrees, adjacent_length):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate the hypotenuse using the cosine function
    hypotenuse_length = adjacent_length / math.cos(angle_radians)
    
    return hypotenuse_length

def main():
    # Prompt the user for the nearest angle in degrees
    angle_degrees = float(input("Enter the nearest angle in degrees: "))
    
    # Prompt the user for the length of the adjacent side
    adjacent_length = float(input("Enter the length of the adjacent side: "))
    
    # Calculate the hypotenuse
    hypotenuse_length = calculate_hypotenuse(angle_degrees, adjacent_length)
    
    # Display the result
    print(f"The length of the hypotenuse is: {hypotenuse_length:.2f}")

if __name__ == "__main__":
    main()
