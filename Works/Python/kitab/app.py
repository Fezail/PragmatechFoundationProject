kitab={
    'ad': "" ,
    'yazan': "",
    'il': "" ,
    'sehifesayi': "" 
}
a=[]
def Showbook():
    for key,val in kitab.items():
        print(key,": ",val)

Showbook()

def changebook():
    kitab["ad"]=input("Bawqa kitab adi yaz: ")
    for key,val in kitab.items():
        print(key,": ",val)
        break
    
changebook()