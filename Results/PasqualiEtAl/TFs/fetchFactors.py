
# Import
import os
import sys

# Input
inputList=[
  "/hpcwork/izkf/projects/malmo/Enrichment/AllPromoters/coexpressed_genes_format/coexpressed_genes_promoter_500/mpbs.bb"
]
factorDict = dict([("FOXP2",["MA0030.1.FOXF2","MA0031.1.FOXD1","MA0480.1.Foxo1","MA0593.1.FOXP2"]),
                   ("BARX2",["UP00151_1_Barx2_3447.2"]),
                   ("PDX1",["MA0125.1.Nobox","MA0132.1.Pdx1","UP00126_1_Dlx2_2273.2","UP00202_1_Dlx1_1741.2"]),
                   ("SOX5",["MA0084.1.SRY","MA0087.1.Sox5","UP00016_1_Sry_primary","UP00030_1_Sox11_primary",
                            "UP00091_1_Sox5_primary","UP00101_1_Sox12_primary"]),
                   ("NKX6-1",["UP00200_1_Nkx6-1_2825.1"])])
outputLocation = "/hpcwork/izkf/projects/malmo/PasqualiEtAl/TFs/Input/"

# Iterating on input list
for inFileName in inputList:

  # Converting to bed
  bedFileName = inFileName[:-2]+"bed"
  os.system("bigBedToBed "+inFileName+" "+bedFileName)

  # Iterating on TFs
  for factor in factorDict.keys():

    # Creating factor dictionary
    factorDictTemp = dict([(e,True) for e in factorDict[factor]])

    # Iterating on inFileName
    outputFileName = outputLocation+factor+"_"+inFileName.split("/")[-2]+".bed"
    outputFile = open(outputFileName,"w")
    inFile = open(bedFileName,"r")
    for line in inFile:
      ll = line.strip().split()
      try: v = factorDictTemp[ll[3]]
      except Exception: continue
      outputFile.write(line)
    inFile.close()
    outputFile.close()

  # Removing bed
  os.system("rm "+bedFileName)


