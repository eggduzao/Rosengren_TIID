###############################################################################
# Gets the promoter regions of a given gene list
###############################################################################

# Import
import os
import sys

# Input
geneListFileName = sys.argv[1]
assocFileName = sys.argv[2]
outputFileName = sys.argv[3]

# Parameters
promoterLen = 500

# Fetching gene list
geneDict = dict()
geneListFile = open(geneListFileName,"r")
for line in geneListFile: geneDict[line.strip()] = True
geneListFile.close()

# Fetching promoter regions
promoterFileName_raw = outputFileName+"_raw"
promoterFile_raw = open(promoterFileName_raw,"w")
assocFile = open(assocFileName,"r")
for line in assocFile:
  ll = line.strip().split("\t")
  if(ll[0] == "chrY"): continue
  try:
    test = geneDict[ll[3]]
    continue
  except Exception: pass
  if(ll[5] == "+"):
    p2 = int(ll[1])
    p1 = p2 - promoterLen
  else:
    p1 = int(ll[2])-1
    p2 = p1 + promoterLen
  promoterFile_raw.write("\t".join([ll[0],str(p1),str(p2)])+"\n")
promoterFile_raw.close()
assocFile.close()

# Sorting promoter file
promoterFileName_sort = outputFileName+"_sort"
os.system(" ".join(["sort -k1,1 -k2,2n",promoterFileName_raw,">",promoterFileName_sort]))

# Merging promoter file
os.system(" ".join(["mergeBed","-i",promoterFileName_sort,">",outputFileName]))

# Removing temp files
os.system(" ".join(["rm",promoterFileName_raw,promoterFileName_sort]))


