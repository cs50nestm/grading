import csv
import os

# --- Prompt user for ZipGrade file name and check if it exists ---
while True:
    zipgrade_filename = input("Enter the name of the ZipGrade CSV file: ").strip()
    if not zipgrade_filename.endswith('.csv'):
        zipgrade_filename += ".csv"
        print(zipgrade_filename)
    # Check if the file exists
    if os.path.isfile(zipgrade_filename):
        break
    else:
        print(f"Error: '{zipgrade_filename}' not found. Please enter a valid file name.")

# --- Read the content of the ZipGrade CSV file ---
with open(zipgrade_filename, 'r') as file:
    reader = csv.reader(file)
    zipgrade_data = list(reader)

# --- Extract the header and data rows ---
header = zipgrade_data[0]
data_rows = zipgrade_data[1:]

# --- Create a dictionary to map student names to their scores ---
class_section = {}
for row in data_rows:
    student_name = f"{row[5]}, {row[4]} ({row[2]})"
    student_score = row[7]
    class_section[student_name] = student_score

# --- Get assignment info for the top of the Jupiter file ---
assignment = input("Assignment Name: ")
date = "(" + input("Due Date: ") + ")"
possible = input("Out of how many points: ")

# --- Ask for name of output file ---
output_filename = input("Enter the name of the output CSV file: ").strip() + ".csv"
if not output_filename.endswith('.csv'):
    output_filename += ".csv"

# --- Write the transformed lines to a new CSV file for Jupiter Grades ---
output_filename = output_filename.replace(" ", "_")

with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write Jupiter import instructions
    writer.writerow(["This file should be opened in a spreadsheet application."])
    writer.writerow(["To import back into Jupiter, save this file as CSV (comma delimited)."])
    writer.writerow(["You may edit scores and add assignment columns, but do not change anything else."])

    writer.writerow([])
    writer.writerow([])

    # Write class info and assignment details
    # Class info must match class name in Jupiter
    class_info = "AP COMP SCI PRINCIP 2 OF 2 (5)"
    writer.writerow(["Class:", class_info])
    writer.writerow(["Assignment:", assignment, ""])
    writer.writerow(["Date:", date, ""])
    writer.writerow(["Possible:", possible, ""])
    writer.writerow(["", "Score:", "Comment:"])

    # Write student scores
    for student_name, student_score in class_section.items():
        writer.writerow([student_name, student_score, ""])

# --- Notify the user that the transformation is complete ---
print(f"The CSV file '{output_filename}' has been successfully transformed.")