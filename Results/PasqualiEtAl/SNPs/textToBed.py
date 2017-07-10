# This script will convert the text files to a bed file.
# It will also standardize scores and use them as a track for IGV.

# Import
import os
import sys
import math

# Input
fileNamePrefix = "SOX5"

#################################################
# Chromatin
#################################################

# Input
inputFileName = "/hpcwork/izkf/projects/malmo/PasqualiEtAl/"+fileNamePrefix+"_chrom.txt"
outputFileName = "/hpcwork/izkf/projects/malmo/PasqualiEtAl/"+fileNamePrefix+"_chrom.bed"
colorDict={"C1":"150,0,0","C2":"0,150,0","C3":"0,0,150","C3c":"150,0,150","C4":"150,150,0","C5":"0,150,150"}

# Execution
inputFile = open(inputFileName,"r")
outputFile = open(outputFileName,"w")
outputFile.write("track name="+fileNamePrefix+"_chrom description=\"Chromatin Domains\" itemRgb=\"On\"\n")
for line in inputFile:
  if(line[0] == "#" or len(line) < 2): continue
  ll = line.strip().split("\t")
  chrName = ll[0]
  pos1 = ll[1]
  pos2 = ll[2]
  ck = ll[3]
  name = "_".join([e for e in ll[3:] if e!="-"])
  outputFile.write("\t".join([chrName,pos1,pos2,name,"1000",".",pos1,pos2,colorDict[ck]])+"\n")
inputFile.close()
outputFile.close()

#################################################
# SNPs
#################################################

# Input
inputFileName = "/hpcwork/izkf/projects/malmo/PasqualiEtAl/"+fileNamePrefix+"_snp.txt"
outputFileName = "/hpcwork/izkf/projects/malmo/PasqualiEtAl/"+fileNamePrefix+"_snp.bed"

# Fetching scores
inputFile = open(inputFileName,"r")
scoreVec = []; maxV = -1; minV = 99
for line in inputFile:
  if(line[0] == "#" or len(line) < 2): continue
  ll = line.strip().split("\t")
  score = -math.log(float(ll[3]),10)
  if(score < minV): minV = score
  if(score > maxV): maxV = score
  scoreVec.append(score)
inputFile.close()

# Standardizing scores
for i in range(0,len(scoreVec)): scoreVec[i] = str(int((scoreVec[i]-minV)*1000/(maxV-minV)))

# Execution
inputFile = open(inputFileName,"r")
outputFile = open(outputFileName,"w")
outputFile.write("track name="+fileNamePrefix+"_snp description=\"SNPs\" useScore=1\n")
counter = 0
for line in inputFile:
  if(line[0] == "#" or len(line) < 2): continue
  ll = line.strip().split("\t")
  chrName = ll[1]
  pos1 = str(int(ll[2])-1)
  pos2 = ll[2]
  name = ll[0]+"_"+ll[3]
  score = scoreVec[counter]
  outputFile.write("\t".join([chrName,pos1,pos2,name,score,".",pos1,pos2,"0,0,0"])+"\n")
  counter += 1
inputFile.close()
outputFile.close()


