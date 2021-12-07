kitab={
    'ad': "Gəncəli müdrik" ,
    'yazar': "Əlisa Nicat",
    'capİli': "1990-cı il" ,
    'sehifesayi': "334" 
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