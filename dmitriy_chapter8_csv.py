import csv

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Open the file in write mode and create a csv writer object
with open('grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
    
    # Get student details and write them to the file
    for _ in range(num_students):
        first_name = input("Enter the student's first name: ")
        last_name = input("Enter the student's last name: ")
        exam1 = int(input("Enter the grade for Exam 1: "))
        exam2 = int(input("Enter the grade for Exam 2: "))
        exam3 = int(input("Enter the grade for Exam 3: "))
        
        writer.writerow([first_name, last_name, exam1, exam2, exam3])

print("Grades have been saved to grades.csv")


import csv

# Open the file in read mode and create a csv reader object
with open('grades.csv', mode='r') as file:
    reader = csv.reader(file)
    # Read the header
    header = next(reader)
    # Print the header
    print(f"{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")
    print("-" * 60)
    
    # Read and print each row of the file
    for row in reader:
        print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")

print("Grades have been displayed.")
    

 