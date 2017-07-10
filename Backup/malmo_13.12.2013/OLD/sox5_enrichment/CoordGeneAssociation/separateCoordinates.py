
# Import
import os
import sys

# Execution
inputList = ["ds","sd"]
motifDictList = []
for inputName in inputList:
    inputFile = open("./"+inputName+"/coord_association.bed","r")
    outputFile = open("./"+inputName+".bed","w")
    motifDictList.append(dict())
    for line in inputFile:
        ll = line.strip().split("\t")
        if(ll[8] == "0,130,0"):
            outputFile.write(line)
            for e in ll[3].split(":"): motifDictList[-1][e.split("_")[0]] = True
    inputFile.close()
    outputFile.close()

# Writing genes that matched report
inputFile = open("/hpcwork/izkf/projects/malmo/sox5_enrichment/CoordGeneAssociation/candidate_genes_format.txt","r")
outputFile = open("/hpcwork/izkf/projects/malmo/sox5_enrichment/CoordGeneAssociation/report.txt","w")
outputFile.write("Gene\tds\tsd\n")
for line in inputFile:
    motif = line.strip()
    printVec = [motif]
    for i in range(0,len(motifDictList)):
        if(motif in motifDictList[i].keys()): printVec.append("Y")
        else: printVec.append("N")
    outputFile.write("\t".join(printVec)+"\n")
inputFile.close()
outputFile.close()


