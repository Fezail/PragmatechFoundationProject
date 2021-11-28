import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
class Register():

    def __init__(self,name="fezail",surname="mahmudov",email="fezail@gmail.com",phone="0501234567",password="12345678",qisamelumat="fezailmelumat"):
        self.name=name
        self.surname=surname
        self.email=email
        self.phone=phone
        self.password=password
        self.qisamelumat=qisamelumat

    def Username(self):
        self.name=input(str("Adi daxil edin: "))
        if self.name != "" :
            print("duzgundur")
        else:
            print('Bu xana bosh olmaz')

    def Surname_(self):
        self.surname=input(str("Soyadini daxil edin: "))
        if self.surname != "":
            print("duzgundur")
        else:
            print('Doldurmaq zeruridir')
    def Mailiyaz(self):
        self.email=input(str("E-mail daxil et: "))
        if (re.search(regex,self.email)):
            print("Duzdur")
        else:
            print("Sehvdir")


    def paSSword(self):
        self.password=input(str("Parolu daxil et: "))
        val = True

        if len(self.password) < 8:
            print('Minimum 8 xarakterden ibaret olmalidir')
            val = False

        if len(self.password) > 20:
            print('Maksimum 20 xarakterden ibaret olmalidir')
            val = False

        if not any(char.isdigit() for char in self.password):
            print('Daxilinde mutleq bir reqem olmalidir')
            val = False

        if not any(char.isupper() for char in self.password):
            print('Minimum bir eded boyuk herf olmalidir.')
            val = False

        if not any(char.islower() for char in self.password):
                print('Minimum bir eded kicik herf olmalidir')
                val = False
        if val:
            return val


# user=Register("Fezail","Mahmudov","fezail@gmail.com","055-555-55-55","1234567","Necesen")
qeyd=Register()
qeyd.Username()
qeyd.Surname_()
qeyd.Mailiyaz()
qeyd.paSSword()