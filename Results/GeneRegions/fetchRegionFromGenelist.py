
# Import
import os
import sys

# Input
regionFileName = "./gene_regions.bed"
geneListFileName = "../GeneLists/coexpressed_genes_format.txt"

# Reading genes to dictionary
geneDict = dict()
geneListFile = open(geneListFileName,"r")
for line in geneListFile: geneDict[line.strip()] = True
geneListFile.close()

# Writing regions
outputFileName = "./"+geneListFileName.split("/")[-1].split(".")[0]+".bed"
outputFile = open(outputFileName,"w")
regionFile = open(regionFileName,"r")
for line in regionFile:
  ll = line.strip().split("\t")
  try: k = geneDict[ll[3]]
  except Exception: continue
  outputFile.write(line)
outputFile.close()


