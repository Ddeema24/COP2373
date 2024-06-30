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
    