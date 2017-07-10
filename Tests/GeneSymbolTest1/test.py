import os
import sys

f = open("association_file_upper.bed")
aDict = dict([(e.split("\t")[3],True) for e in f])
f.close()

f = open("coexpressed_genes_format.txt")
allList = [e.strip() for e in f]
f.close()

for e in allList:
    try:
        x = aDict[e]
    except Exception:
        print e

