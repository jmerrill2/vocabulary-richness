from nltk.stem.porter import PorterStemmer
from itertools import groupby
import sys

def words(entry):
    words = filter(lambda w: len(w) > 0, [w.strip("0123456789!:,.?(){}[]") for w in entry.split()])
    return words


def yule(entry):
    # yule's I measure (the inverse of yule's K measure)
    # higher number is higher diversity - richer vocabulary
    d = {}
    stemmer = PorterStemmer()
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1

    M1 = float(len(d))
    M2 = sum([len(list(g)) * (freq ** 2) for freq, g in
              groupby(sorted(d.values()))])

    try:
        val = (M1 * M1) / (M2 - M1)
        print('val: ', val)
        return val
    except ZeroDivisionError:
        print('OOPS, division by 0 error.')
        return 0


if __name__ == '__main__':
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    textfile = sys.argv[1]
    with open(textfile, 'r') as i:
        lines = i.read().replace('\n', '')
    yule(lines)
