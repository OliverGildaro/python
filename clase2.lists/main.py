#lists

student = ["oliver", 'ivan', 'alvar']
student2 = ['amadeo', 'miriam']
student3 = 'borolas'

student.insert(student3)#added to the begining
student.append(student3)#add to the end
student.extend(student2)#add amadeo and miriam like two strings

print(student)