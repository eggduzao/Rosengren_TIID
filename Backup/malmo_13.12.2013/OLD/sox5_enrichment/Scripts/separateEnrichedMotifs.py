########################################################
# Script that gets only the MPBSs that are:
# 1. Enriched in nev and rand.
# 2. Inside coordinates associated with genes (ev).
########################################################

# Import
import os
import sys
import glob

# Input
inLoc = "/hpcwork/izkf/projects/malmo/sox5_enrichment/Results3/"
inList = glob.glob(inLoc+"*/")
cutoff = 0.05

# Iterating on input folders
for inFolder in inList:
    
    # Opening files
    if(len(glob.glob(inFolder+"mpbs.bb")) == 0): continue
    coordName = inFolder.split("/")[-2]
    os.system("bigBedToBed "+inFolder+"mpbs.bb "+inFolder+"mpbs.bed")
    mpbsFile = open(inFolder+"mpbs.bed","r")
    nevFile = open(inFolder+"nev_1_statistics.txt","r")
    randFile = open(inFolder+"rand_1_statistics.txt","r")
    outputFileNev = open(inFolder+"nev_"+coordName+"_enrichedTF.bed","w")
    outputFileRand = open(inFolder+"rand_"+coordName+"_enrichedTF.bed","w")
    inFileList = [nevFile,randFile]
    outFileList = [outputFileNev,outputFileRand]

    # Creating enriched dictionaries
    enrichDictList = []
    for inFile in inFileList:
        enrichDictList.append(dict())
        inFile.readline()
        for line in inFile:
            ll = line.strip().split("\t")
            if(float(ll[2]) <= cutoff): enrichDictList[-1][ll[0]] = True
            else: enrichDictList[-1][ll[0]] = False

    # Iterating on mpbs
    for line in mpbsFile:
        ll = line.strip().split("\t")
        if(ll[-1] != "0,130,0"): continue
        for i in range(0,len(outFileList)):
            if(enrichDictList[i][ll[3]]): outFileList[i].write(line)

    # Termination
    os.system("rm "+inFolder+"mpbs.bed")
    mpbsFile.close()
    nevFile.close()
    randFile.close()
    outputFileNev.close()
    outputFileRand.close()


