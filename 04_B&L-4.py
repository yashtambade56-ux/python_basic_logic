# Input marks of 5 subjects; print total, average, and percentage.

print("entermarks for five subjects(out of 100):")
subject1 = int(input("maths: "))
subject2 = int(input("eng: "))
subject3 = int(input("sci: "))
subject4 = int(input("hist: "))
subject5 = int(input("geo: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100
average_marks = total_marks / 5

print("-----RESULT-----")
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage}%")
print(f"Average Marks: {average_marks}")