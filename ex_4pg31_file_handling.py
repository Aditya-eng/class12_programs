myfile = open ("book.txt","a")
ans="y"
while ans=='y':
  bno = int(input("Enter book number "))
  bname = input("Enter Book Name ")
  author = input("Enter Author Name ")
  price = int(input("Enter Book Price "))
  brec = str (bno) + "," + bname +","+author+","+str(price)+"\n"
  myfile.write(brec)
  ans=input("Add More ?")
myfile.close()