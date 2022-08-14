class Cuzhi:
    def __init__(self, naili, douxing, shouming, qishi, jiaoli, yaqian, baojigailv,
                 baojizengshang, jishanggailv, gedanggailv, gedangshuzhi, fanjigailv,
                 name):
        self.naili = naili
        self.douxing = douxing
        self.shouming = shouming
        self.qishi = qishi
        self.jiaoli = jiaoli
        self.yaqian = yaqian
        self.baojigailv = baojigailv
        self.baojizengshang = baojizengshang
        self.jishanggailv = jishanggailv
        self.gedanggailv = gedanggailv
        self.gedangshuzhi = gedangshuzhi
        self.fanjigailv = fanjigailv
        self.name = name

    def __str__(self):
        return self.name

    def take_damage_naili(self, damage: int, round_object):
        self.naili -= damage
        if self.naili <= 0:
            round_object.end(self)

    def take_damage_douxing(self, damage: int, round_object):
        self.douxing -= damage
        if self.douxing <= 0:
            round_object.end(self)
