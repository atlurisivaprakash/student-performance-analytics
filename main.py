import pandas as pd
import numpy as np


# Function to assign grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to calculate pass/fail
def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Read student data
data = pd.read_csv("students.csv")

print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====\n")

print("Student Data:")
print(data)


# Calculate total marks using NumPy
data["Total"] = np.sum(
    data[["Python", "Maths", "DBMS"]].values,
    axis=1
)

# Calculate average marks
data["Average"] = data["Total"] / 3

# Assign grades
data["Grade"] = data["Average"].apply(calculate_grade)

# Determine pass/fail
data["Result"] = data["Average"].apply(check_result)


# Display complete analysis
print("\n===== STUDENT ANALYSIS =====")
print(data[[
    "Student_ID",
    "Name",
    "Total",
    "Average",
    "Grade",
    "Result"
]])


# Highest and lowest performance
highest = data["Average"].max()
lowest = data["Average"].min()

highest_student = data.loc[data["Average"].idxmax(), "Name"]
lowest_student = data.loc[data["Average"].idxmin(), "Name"]

print("\n===== PERFORMANCE SUMMARY =====")
print("Highest Average:", highest)
print("Top Student:", highest_student)
print("Lowest Average:", lowest)
print("Lowest Performing Student:", lowest_student)


# Overall class average
class_average = np.mean(data["Average"])

print("Overall Class Average:", round(class_average, 2))


# Pass and fail statistics
pass_count = (data["Result"] == "Pass").sum()
fail_count = (data["Result"] == "Fail").sum()

print("\n===== PASS / FAIL STATISTICS =====")
print("Number of Students Passed:", pass_count)
print("Number of Students Failed:", fail_count)


# Subject-wise average
print("\n===== SUBJECT-WISE PERFORMANCE =====")

subjects = ["Python", "Maths", "DBMS"]

for subject in subjects:
    average = np.mean(data[subject])
    print(subject, "Average:", round(average, 2))


# Top 5 performers
print("\n===== TOP 5 PERFORMERS =====")

top_students = data.sort_values(
    by="Average",
    ascending=False
).head(5)

print(top_students[[
    "Student_ID",
    "Name",
    "Average",
    "Grade"
]])