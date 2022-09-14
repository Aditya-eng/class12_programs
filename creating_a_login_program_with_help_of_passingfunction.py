def loginCheck(users,passwords,inputuser,inputpassword) :
    index = None
    password = None
    if inputuser in users:
        index = users.index(inputuser)
        password = passwords[index]
        if password==inputpassword:
            return "Login Successful!"
        else:
            return "Invalid Pasword Entered"
    else:
            return "Invaid User Name"
usernames=( 'Admin' , 'System' , 'Guest ')
passwords= ('admini123 ' , 'manager' , 'guest')
print (". . : : : Login ")
print("*************")
u = input("Enter User Name: ")
p = input("Enter Password: ")
response = loginCheck (usernames, passwords,u, p)
print (response)