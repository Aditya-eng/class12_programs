#Practical implementation 13
#To pass student record as a dictionary and update their mistakes

def marks_increase(stud,P):
    stud["Marks"] +=P
    stud["Status"] = "Updated"

student1 = {"Roll_no.":1,"Name":"Radhika","Marks":89,"Status":"+"}
student2 = {"Roll_no":4,"Name":"Shaurya","Marks":90,"Status":"+"}
marks_increase(student1,50)
marks_increase(student2,60)
print(student1)
print(student2)


