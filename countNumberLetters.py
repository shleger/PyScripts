__author__ = 'shleger'

# from num2word.num2word_EN import n2w, to_card, to_ord, to_ordnum
from  num2words.num2word_EN_GB import to_card
import re


MAX_VAL = 1000
sum = 0

for i in range(1, MAX_VAL + 1):
    s = re.sub('[\s,-]', '', to_card(i))
    sum += s.__len__()
    print i.__str__() + " " + sum.__str__()

