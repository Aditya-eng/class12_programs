import pickle
def read():
    f=open("Binaryfile","rb")
    Rec = pickle.load(f)
    print(Rec)
    #print(Rec,rec2,rec3)
    f.close()


read()






