wildcard = 2
def gamedone(p1, p2, p3, p4, p5, p6, p7, p1name, p2name, p3name, p4name, p5name, p6name, p7name, player1playing, player2playing, player3playing, player4playing, player5playing, player6playing, player7playing):
    if len(player1playing) == 3:
        print(p1name, 'score was', p1.cs)
        if len(player2playing) == 3:
            print(p2name, 'score was', p2.cs)
            if len(player3playing) == 3:
                print(p3name, 'score was', p3.cs)
                if len(player4playing) == 3:
                    print(p4name, 'score was', p4.cs)
                    if len(player5playing) == 3:
                        print(p5name, 'score was', p5.cs)
                        if len(player6playing) == 3:
                            print(p6name, 'score was', p6.cs)
                            if len(player7playing) == 3:
                                print(p7name, 'score was', p7.cs)
def read(score,player):
    print('Please place your card to read')
    try:
        player1 = player
        score =  input("Add: ")#reader.read()
        player1.add(score)
    except:
        print('Please place card to read')
class score:
    def __init__(self, cs, name):
        self.cs = cs
        self.name = name
    def add(self, score):
        self.cs += score
    def name(self, name):
        self.name = name
    def read(self):
        self.cs += int(input("Add: "))
        print(self.cs)
class wild:
    def __init__(self, cw):
        self.cw = cw
    def add(self):
        self.cw += 1