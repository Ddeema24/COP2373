import csv
from statistics import mean, median, stdev, StatisticsError

# File path to the CSV
file_path = 'grades.csv'

# Load the data from the CSV file
data = []
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip the header
    for row in reader:
        try:
            # Convert each value to float and handle non-numeric values
            numeric_values = [float(value) for value in row[2:]]  # Assuming grades start from the third column
            data.append(numeric_values)
        except ValueError:
            print(f"Warning: Skipping row due to non-numeric values: {row}")

# Convert data to a list of columns
if data:
    data = list(zip(*data))

    # Print the first few rows of the dataset
    print("First few rows of the dataset:")
    first_few_rows = [list(row)[:5] for row in zip(*data)]
    for i, row in enumerate(first_few_rows):
        print(f"Row {i + 1}: {row}")

    # Calculate and print the statistics for each exam (columns)
    num_exams = len(data)  # Number of exams (columns)

    for i in range(num_exams):
        exam_data = data[i]
        try:
            print(f"\nStatistics for Exam {i + 1}:")
            print(f"Mean: {mean(exam_data):.2f}")
            print(f"Median: {median(exam_data):.2f}")
            print(f"Standard Deviation: {stdev(exam_data):.2f}")
            print(f"Minimum: {min(exam_data):.2f}")
            print(f"Maximum: {max(exam_data):.2f}")
        except StatisticsError:
            print(f"Statistics cannot be calculated for Exam {i + 1}: Not enough data")

    # Calculate and print the overall statistics for the entire dataset (all exams combined)
    all_grades = [grade for sublist in data for grade in sublist]

    if all_grades:
        print("\nOverall Statistics for All Exams Combined:")
        try:
            print(f"Mean: {mean(all_grades):.2f}")
            print(f"Median: {median(all_grades):.2f}")
            print(f"Standard Deviation: {stdev(all_grades):.2f}")
            print(f"Minimum: {min(all_grades):.2f}")
            print(f"Maximum: {max(all_grades):.2f}")
        except StatisticsError:
            print("Statistics cannot be calculated: Not enough data")

    # Determine and print the number of students who passed and failed each exam
    passing_grade = 60
    for i in range(num_exams):
        exam_data = data[i]
        passed = sum(grade >= passing_grade for grade in exam_data)
        failed = len(exam_data) - passed
        print(f"\nExam {i + 1}: {passed} students passed, {failed} students failed")

    # Calculate and print the overall pass percentage across all exams
    total_grades = len(all_grades)
    passing_grades = sum(grade >= passing_grade for grade in all_grades)
    pass_percentage = (passing_grades / total_grades) * 100 if total_grades > 0 else 0
    print(f"\nOverall pass percentage across all exams: {pass_percentage:.2f}%")

else:
    print("No valid numeric data found.")









