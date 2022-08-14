from Cuzhi import Cuzhi
from Round import Round
from cuzhi_data import cuzhi_data
from random import random
import math

# c1 = cuzhi_data[math.floor(random() * 50)]
# c2 = cuzhi_data[math.floor(random() * 50)]
c1 = cuzhi_data[0]
c2 = cuzhi_data[5]

c1_count = 0
c2_count = 0

for i in range(1000):
    cricket1 = Cuzhi(*c1)
    cricket2 = Cuzhi(*c2)
    test_round = Round(cricket1, cricket2)
    winner = test_round.fight()
    if winner == cricket1:
        c1_count += 1
    elif winner == cricket2:
        c2_count += 1

print({c1[-1]: c1_count, c2[-1]: c2_count})
