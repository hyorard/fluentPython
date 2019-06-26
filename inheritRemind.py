class pro():
    height = 0
    weight = 0
    nation = None
    pos = None
    name = None
    rep = "4th division"
    
    def __init__(self, name = None, height = 180, weight = 70):
        self.name = name
        self.height = height
        self.weight = weight
        if self.name == "Steven Gerrard":
            self.rep = "World Class Player"
    
    def setPos(self, pos = "fullBack"):
        self.pos = pos

    def setNation(self, nation = None):
        self.nation = nation
        if self.nation == "Korea":
            self.rep = "K league Classic"
    
    def showProfile(self):
        print("{0}'s profile".format(self.name))
        print("name = {0}, height = {1}, weight = {2}, nation = {3}, position = {4}, rep = {5}".format(self.name,self.height,self.weight,self.nation,self.pos,self.rep))
        print()

class ama(pro):
    rep = "amatuer"
    col = None

    def setCollege(self, col = "고졸"):
        self.col = col
    
    def checkPotential(self):
        if self.name == "Hyorard":
            self.rep = "제 2의 Steven Gerrard"
            print("{0} {1}라고 알려져 있습니다.".format(self.col,self.rep))
            print()

StevieG = pro("Steven Gerrard", 183, 83)
StevieG.setPos("AllRound Player")
StevieG.setNation("England")
StevieG.showProfile()

HyoSeongKim = ama("Hyorard", 173.9, 74)
HyoSeongKim.setPos("cm, am, dcm, lw, rw, lb, rb")
HyoSeongKim.setNation("Korea")
HyoSeongKim.setCollege("외대")
HyoSeongKim.showProfile()
HyoSeongKim.checkPotential()
        

    