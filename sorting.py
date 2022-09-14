import pickle
def sort():
    f = open("Binaryfile","rb+")
    Rec=  pickle.load(f)
    Rec.sort(key=lambda Rec:Rec[0])
    f.seek(0)
    pickle.dump(Rec,f)
    f.close()

def write():
    f=open("Binaryfile","wb")
    Rec=[]
    while True:
        github_id=input("Enter GITHUB_ID: ")
        name = input("Enter Name: ")
        per_site = input("Enter personal website url: ")
        R=[github_id,name,per_site]
        Rec.append(R)
        ch=input("more records: ")
        if ch.upper()=="N":
            break
    pickle.dump(Rec,f)
    f.close()

def read():
    f=open("Binaryfile","rb")
    Rec = pickle.load(f)
    print(Rec)
    f.close()

write()
read()
sort()

