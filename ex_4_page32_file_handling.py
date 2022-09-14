myfile0 = open("book.txt","w")
myfile0.write("sample text")
myfile1=open ("book.txt","r")
myfile2 = open("book_backup.txt",'w')
str1 = " "
while str1:
    str1 = myfile1.readline()
    myfile2.write(str1)
# myfile2.close()
# myfile1.close()
#myfile0.close()
print("Coppied !!!!!!!!!!!!!!!!!!!!!!!")