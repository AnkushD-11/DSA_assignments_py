#Write a program to collect height and weights of N students. Find highest weight/height ratio.

# Function to calculate weight-to-height ratio
def calculate_ratio(weight, height):
    return weight / height

# Input the number of students
N = int(input("Enter the number of students: "))

# Initialize variables to store the information of the student with the highest ratio
max_ratio = 0
max_student = None

# Collect height and weight data for each student and find the highest ratio
for i in range(N):
    print(f"Enter data for student {i+1}:")
    weight = float(input("Enter weight (in kilograms): "))
    height = float(input("Enter height (in meters): "))
    
    ratio = calculate_ratio(weight, height)
    
    if ratio > max_ratio:
        max_ratio = ratio
        max_student = (weight, height, i+1)

# Display the student with the highest ratio
if max_student is not None:
    max_weight, max_height, student_number = max_student
    print(f"Student {student_number} has the highest weight-to-height ratio of {max_ratio:.2f}.")
    print(f"Weight: {max_weight} kg, Height: {max_height} m")
else:
    print("No data entered.")
