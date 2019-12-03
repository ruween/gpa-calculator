import numpy as np 

#Author : Ruween Iddagoda - https://www.linkedin.com/in/ruween-iddagoda-b2400a181

grading_scale = {"A+" : 4, "A" : 4, "A-" : 3.7, "B+" : 3.3, "B" : 3.0, "B-" : 2.7, "C+" : 2.3, "C" : 2.0, "C-" : 1.7, "D" : 1.3, "D-" : 1.0, "E" : 0 }

print("[+] Welcome to GPA Calculator")
 
no_of_modules = int(input("Enter the number of modules you took: "))

weights = []
grades = []

for i in range(no_of_modules):
    grade_string = input("Enter your GRADE for module " + str(i+1) + " : ")
    weight = input("Enter the WEIGHT of the module " + str(i+1) + " : ")
    weights.append(float(weight))
    if grade_string in grading_scale:
        grade = grading_scale[grade_string]
        grades.append(float(grade))
    else:
        print("Invalid Character")
    
    

weights_array = np.array([weights])
grades_array = np.array([grades])

temp_array1 = np.dot(weights_array,grades_array.T)
temp_array = float(np.sum(temp_array1))
total_points_earned = temp_array
total_weights = float(np.sum(weights_array))

GPA = total_points_earned / total_weights

print("-----------------------")
print("[+] Your GPA is: {:,.2f}".format(GPA))
print("-----------------------")


