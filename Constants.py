from enum import Enum


class Constants:
    XIANSHOU_QISHI_DIFF = 0.8
    XIANSHOU_QISHI_SAME = 0.5
    JISHANG_NAILI_DOUXING = 0.65
    JISHANG_NAILI_DOUXING_VALUE = 5
    JISHANG_QISHI_YAQIAN_JIAOLI_VALUE = 1


class AttackType(Enum):
    QISHI = 1
    YAQIAN = 2
    JIAOLI = 3
    BAOJIZENGSHANG = 4
