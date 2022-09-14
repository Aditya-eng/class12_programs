myfile = open("ipl.txt")
# myfile.write('''sampletext thgfdh "
#              "hgfhgfhgfh''')
line1 = myfile.readline()
print("Length of line:",len(line1))
line1 = line1.rstrip('/n')
print("Length of line: ",len(line1))
line2 = myfile.readline()
print("Length of line is : ",len(line2))
line2 = line2.lstrip()  
print("Length of line2 is : ",len(line2))






