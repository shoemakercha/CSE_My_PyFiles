from __future__ import print_function 
Semester_Grade = int(raw_input("Enter Semester Grade:"))
Final_Exam_Grade = int(raw_input("Enter Final Exam Grade:"))
Final_Exam_Weight = int(raw_input("Enter Final Exam Weight:"))
Final_Grade = (Semester_Grade * (100 - Final_Exam_Weight)) + (Final_Exam_Grade * Final_Exam_Weight)
print( Final_Grade / 100. , "%")
