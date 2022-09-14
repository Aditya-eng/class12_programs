def updatevalue (myd, key,name) :
    myd[key] = name
student={"roll":1,"name":"amit","per":89}
print(student)
print("1_ Change roll")
print("2. change name")
print("3. change percentage")
choice=int(input('£nter your choice :*'))
key=None
if choice==1:
    r = int(input("Enter the new roll number: "))
    key = "roll"
elif choice ==2:
    r = input("Enter new name: ")
    key='name'
elif choice ==3:
    r=int(input("Enter new percentage :"))
    key='per'
else:
    print("Invalid choice i")
if key !=None:
    updatevalue(student,key, r )
print(student)