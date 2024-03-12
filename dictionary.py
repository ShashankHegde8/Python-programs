d=dict()
class employee:
    def input(self):
        self.name=input("enter your name")
        self.address=input("enter address")
        self.basic=int(input("enter basic salary"))
        self.tds=int(input("enter tds"))
        self.da=0.10*self.basic
        self.hra=0.25*self.basic
        self.deduct=0.2*self.basic
        self.gross=self.basic+self.hra+self.da+self.tds
        self.net= self.gross-self.deduct
        self.update()
    def update(self):
        d.ipdate({self.name:{
            "name":self.name,
            "address":self.address,
            "basic":self.basic,
            "tds":self.tds,
            "da":self.da,
            "deduct":self.deduct,
            "gross":self.gross,
            "net":self.net
        }})
    def search(self,name):
        f=0
        for key in d:
            if key == name:
                f=1
                print("employee found")
                for i in d:
                    print(i,d[key][i])
        if f == 0:
            print("Employee not found")

    def display(self):
        for i in d:
            print(i,d[i])
em=employee()
g=1
while(g):
    print("1.add \n 2. search \n 3. display\n 4.exit" )
    ch=int(input("enter choice "))
    if(ch == 1):
        em.input()
    elif(ch == 2):
        n=input("enter name")
        em.search(n)
    elif(ch == 3):
        em.display()
    elif(ch == 4):
        g=0
    else:
        print("wrong choice")
