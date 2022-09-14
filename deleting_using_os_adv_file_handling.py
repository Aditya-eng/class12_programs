import pickle
import os
def Del( ):
    f=open( "Binaryfile", "rb")
    f1=open( "Temp", "wb")
    a=input("Enter the github_id to be deleted: ")
    found=0
    try:
        while True:
            Rec=pickle.load(f)
            if Rec[0]==a:
                found+=1
            else:
                pickle.dump (Rec, f1)
    except EOFError:
        f.close()
        f1.close()
    if found==0:
        print("Record not found")
    os.remove ("Binaryfile")
    os.rename ("Temp", "Binaryfile")

# def write():
#     f = open("Binaryfile","wb")
#     Rec=[]
#     while True:
#         name = input("Enter your name: ")
#         github_id = input("Enter Github_ID: ")
#         per_site = input("Enter personal website link: ")
#         if per_site[0] + per_site[1] + per_site[2] + per_site[3] == "http" or per_site[0] + per_site[1] + per_site[2] + \
#                 per_site[3] == "www.":
#             continue
#         else:
#             print("warning this is not a url.")
#             R= [github_id,per_site,name]
#             Rec.append(R)
#             ch = input("more records? ")
#             if ch.upper() == "N":
#                 break
#     pickle.dump(Rec,f)
#     f.close()



def write():
    f=open("Binaryfile","wb")
    while True:
        github_id = input("Enter GITHUB_ID: ")
        name = input("Enter Name: ")
        per_site = input("Enter personal website url: ")
        R = [github_id, name, per_site]
        pickle.dump(R,f)
        ch = input("more records:")
        if ch.upper() == "N":
            break
    f.close()

def read():
    f=open("Binaryfile","rb")
    try:
        while True:
            Rec = pickle.load(f)
            print(Rec)
    except EOFError:
        f.close()




write()
read()
Del()
read()