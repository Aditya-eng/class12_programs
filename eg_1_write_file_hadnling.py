myfile = open("studentetzt","a")
for i in range(3):
   name = input("Enter name to store:")
   myfile.write(name)
   myfile.write('\n')
myfile.close()
print("\nData Saved Successfully...")

