from Cuzhi import Cuzhi
import random
from Constants import Constants, AttackType
from enum import Enum


class Result(Enum):
    ONE_WIN = 1
    TWO_WIN = 2
    TIE = 3


class Round:
    def __init__(self, c1: Cuzhi, c2: Cuzhi):
        self.loser: None | Cuzhi = None
        self._c1 = c1
        self._c2 = c2

    def end(self, loser: Cuzhi):
        if self.loser is None:
            self.loser = loser

    @staticmethod
    def roll_probability(probability: float) -> bool:
        return random.random() < probability

    def _attack(self, attacker: Cuzhi, defender: Cuzhi, attack_type: AttackType,
                defended: bool = False):
        gedang = defender.gedangshuzhi if defended else 0
        if attack_type == AttackType.YAQIAN:
            defender.take_damage_naili(attacker.yaqian - gedang, self)
        elif attack_type == AttackType.QISHI:
            defender.take_damage_douxing(attacker.qishi - gedang, self)
        elif attack_type == AttackType.JIAOLI:
            defender.take_damage_naili(attacker.jiaoli - gedang, self)
        elif attack_type == AttackType.BAOJIZENGSHANG:
            defender.take_damage_naili(attacker.baojizengshang, self)

    @staticmethod
    def _jishang(attacker: Cuzhi, defender: Cuzhi):
        if Round.roll_probability(attacker.jishanggailv) and Round.roll_probability(
                attacker.jishanggailv):
            if Round.roll_probability(Constants.JISHANG_NAILI_DOUXING):
                if Round.roll_probability(0.5):
                    defender.naili -= Constants.JISHANG_NAILI_DOUXING_VALUE
                else:
                    defender.douxing -= Constants.JISHANG_NAILI_DOUXING_VALUE
            else:
                probability = random.random()
                if probability < 0.333:
                    defender.yaqian -= Constants.JISHANG_QISHI_YAQIAN_JIAOLI_VALUE
                elif probability < 0.666:
                    defender.qishi -= Constants.JISHANG_QISHI_YAQIAN_JIAOLI_VALUE
                else:
                    defender.jiaoli -= Constants.JISHANG_QISHI_YAQIAN_JIAOLI_VALUE

    def _compare_qishi(self) -> Result:
        if self._c1.qishi > self._c2.qishi:
            return Result.ONE_WIN
        elif self._c1.qishi < self._c2.qishi:
            return Result.TWO_WIN
        else:
            return Result.TIE

    def _qishibipin(self):
        res = self._compare_qishi()
        if res == Result.ONE_WIN:
            self._attack(self._c1, self._c2, AttackType.QISHI)
        elif res == Result.TWO_WIN:
            self._attack(self._c2, self._c1, AttackType.QISHI)

    def _decide_xianshou(self):
        res = self._compare_qishi()
        if res == Result.ONE_WIN:
            c1_xianshou = Round.roll_probability(Constants.XIANSHOU_QISHI_DIFF)
        elif res == Result.TWO_WIN:
            c1_xianshou = Round.roll_probability(1 - Constants.XIANSHOU_QISHI_DIFF)
        else:
            c1_xianshou = Round.roll_probability(Constants.XIANSHOU_QISHI_SAME)
        return c1_xianshou

    def _zhuiji(self, attacker: Cuzhi, defender: Cuzhi):
        self._attack(attacker, defender, AttackType.YAQIAN)
        if Round.roll_probability(defender.fanjigailv):
            self._attack(defender, attacker, AttackType.JIAOLI)

    def _main_phase(self, attacker: Cuzhi, defender: Cuzhi):
        self._qishibipin()
        defender_half = True
        fanji = False
        while True:
            if defender_half:
                attack_type = AttackType.YAQIAN
            else:
                attack_type = AttackType.JIAOLI

            successfully_defended = Round.roll_probability(defender.gedanggailv)

            self._attack(attacker, defender, attack_type, successfully_defended)

            if fanji:
                self._attack(attacker, defender, AttackType.QISHI, successfully_defended)

            if Round.roll_probability(attacker.baojigailv):
                if not fanji:
                    self._attack(attacker, defender, AttackType.QISHI,
                                 successfully_defended)
                self._attack(attacker, defender, AttackType.BAOJIZENGSHANG)

            if not successfully_defended:
                Round._jishang(attacker, defender)

            if Round.roll_probability(defender.fanjigailv):
                fanji = True
                attacker, defender = defender, attacker
                defender_half = not defender_half
            else:
                break

        if fanji:
            self._zhuiji(defender, attacker)

    def _main_round(self, attacker: Cuzhi, defender: Cuzhi):
        while self.loser is None:
            self._main_phase(attacker, defender)
            attacker, defender = defender, attacker

    def _round(self):
        c1_xianshou = self._decide_xianshou()

        if c1_xianshou:
            self._main_round(self._c1, self._c2)
        else:
            self._main_round(self._c2, self._c1)

    def fight(self):
        self._round()
        return self._c1 if self.loser == self._c2 else self._c2
