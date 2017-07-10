import os
import sys
f = open("association_file.bed")
fo = open("association_file_upper.bed","w")
for line in f:
    ll = line.strip().split("\t")
    ll[3] = ll[3].upper()
    fo.write("\t".join(ll)+"\n")
f.close()
fo.close()
