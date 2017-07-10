import os
import sys

f = open("all_genes_format.txt")
aDict = dict([(e.strip(),True) for e in f])
f.close()

f = open("candidate_genes_format_old.txt")
allList = [e.strip() for e in f]
f.close()

for e in allList:
    try:
        x = aDict[e]
    except Exception:
        print e

