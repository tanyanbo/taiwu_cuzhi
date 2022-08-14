from Round import Round


class Cuzhi:
    def __init__(self, naili, douxing, qishi, jiaoli, yaqian, baojigailv,
                 baojizengshang, jishanggailv, gedanggailv, gedangshuzhi, fanjigailv):
        self.naili = naili
        self.douxing = douxing
        self.qishi = qishi
        self.jiaoli = jiaoli
        self.yaqian = yaqian
        self.baojigailv = baojigailv
        self.baojizengshang = baojizengshang
        self.jishanggailv = jishanggailv
        self.gedanggailv = gedanggailv
        self.gedangshuzhi = gedangshuzhi
        self.fanjigailv = fanjigailv

    def take_damage_naili(self, damage: int, round_object: Round):
        self.naili -= damage
        if self.naili <= 0:
            round_object.end(self)

    def take_damage_douxing(self, damage: int, round_object: Round):
        self.douxing -= damage
        if self.douxing <= 0:
            round_object.end(self)
