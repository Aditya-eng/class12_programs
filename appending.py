import pickle

#from torch import per_channel_affine


def app():
    f=open("Binaryfile","rb+")
    Rec = pickle.load(f)
    while True:
        name=input("Enter your name: ")
        github_id = input("Enter Github_ID: ")
        per_site = input("Enter personal website link: ")
        if per_site[0] + per_site[1]+ per_site[2]+per_site[3] == "http" or per_site[0] + per_site[1]+ per_site[2]+per_site[3]=="www.":
            continue
        else:
            print("warning this is not a url.")
        R= [github_id,per_site,name]
        Rec.append(R)
        ch=input("more records? ")
        if ch.upper()=="N":
            break
    f.seek(0)
    pickle.dump(Rec,f)
    f.close()

def write():
    f = open("Binaryfile","wb")
    Rec=[]
    while True:
        name = input("Enter your name: ")
        github_id = input("Enter Github_ID: ")
        per_site = input("Enter personal website link: ")
        if per_site[0] + per_site[1] + per_site[2] + per_site[3] == "http" or per_site[0] + per_site[1] + per_site[2] + \
                per_site[3] == "www.":
            continue
        else:
            print("warning this is not a url.")
            R= [github_id,per_site,name]
            Rec.append(R)
            ch = input("more records? ")
            if ch.upper() == "N":
                break
    pickle.dump(Rec,f)
    f.close()

def read():
    f=open("Binaryfile","rb")
    Rec = pickle.load(f)
    print(Rec)
    f.close()

#write()
read()
#app()