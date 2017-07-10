
# Import
import os
import sys
import glob

# Input
inLoc = "/hpcwork/izkf/projects/malmo/Motif_Matching/Input/"
inputFileList = [ inLoc+"ds.bed", inLoc+"sd.bed" ]
motifLocation = "/work/eg474423/reg-gen/data/PrecomputedMotifs_fdr4/"
outLoc = "/hpcwork/izkf/projects/malmo/Motif_Matching/Results/"

# Iterating on inputFiles:
for inputFileName in inputFileList:

    # Initialization
    inputName = inputFileName.split("/")[-1].split(".")[0]
    outputFileName = outLoc+inputName+".bed"
    outputTemp = outLoc+inputName+"/"
    os.system("mkdir -p "+outputTemp)

    # Iterating on bigbed files of motifLocation
    for motifFileName in glob.glob(motifLocation+"*.bb"):

        # Perform intersectBed
        motifName = ".".join(motifFileName.split("/")[-1].split(".")[:-1])
        inBedFileName = outputTemp+motifName+"_IN.bed"
        outBedFileName = outputTemp+motifName+"_OUT.bed"
        os.system("bigBedToBed "+motifFileName+" "+inBedFileName)
        os.system("intersectBed -a "+inBedFileName+" -b "+inputFileName+" -wa > "+outBedFileName)
        os.system("rm "+inBedFileName)

        # Adjust motif name
        finalBedFileName = outputTemp+motifName+".bed"
        bedFile = open(outBedFileName,"r")
        outBedFile = open(finalBedFileName,"w")
        for line in bedFile:
            ll = line.strip().split("\t")
            outBedFile.write("\t".join(ll[:3]+[motifName]+ll[4:6])+"\n")
        bedFile.close()
        outBedFile.close()
        os.system("rm "+outBedFileName)

    # Concatenating all bed files and removing folder
    os.system("cat "+outputTemp+"*.bed > "+outputFileName)
    os.system("rm -rf "+outputTemp)


