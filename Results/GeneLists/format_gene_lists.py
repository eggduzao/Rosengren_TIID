
# Import
import os
import sys

# Input
geneListSet = [ "/hpcwork/izkf/projects/malmo/GeneLists/all_genes_raw.txt",
                "/hpcwork/izkf/projects/malmo/GeneLists/coexpressed_genes_raw.txt"
]

# Dictionary of symbols
# Uppercase to Uppercase
# These mappings were made using uniprot and genecards
symbolDict = dict([
    # SH
    ("C9ORF150","LURAP1L"),
    ("FAM123C","AMER3"),
    ("FAM148A","C2CD4A"),
    ("KIAA0774","MTUS2"),
    ("KIAA1383","MAP10"),
    ("KIAA1486","NYAP2"),
    ("BRAC","T"),
    ("ODZ3","TENM3"),
    ("BAPX1","NKX3-2"),
    ("CEBP","CPEB1"),
    ("DELTAEF1","ZEB1,ZEB2"),
    # EG
    ("AAA1","SLC7A10"),
    ("C15ORF23","KNSTRN"),
    ("C20ORF54","SLC52A3"),
    ("C6ORF162","SMIM8"),
    ("D4S234E","NSG1"),
    ("EVI1","MECOM"),
    ("FLJ25770","CCDC158"),
    ("GFI","GFI1,GFI1B"),
    ("MS4A8B","MS4A8"),
    ("PBX","PBX1,PBX2,PBX3,PBX4"),
    ("RORA2","RORA"),
    ("TCF1","HNF1A,TCF7"),
    ("TCFE2A","TCF3"),
    ("TEAD","TEAD1,TEAD2,TEAD3,TEAD4,TEAD5"),
    ("ZNF42","MZF1")
])

# Iterate on gene list
for geneListFileName in geneListSet:

    # Read gene list
    geneList = [] # In the end it will be RAW, UPPER, FINAL
    geneListFile = open(geneListFileName,"r")
    for line in geneListFile:
        geneList.append([line.strip(),line.strip().upper()])
    geneListFile.close()

    # Insert correct symbols
    for e in geneList:
        try:
            e.append(symbolDict[e[1]])
        except Exception:
            e.append(e[1])

    # Writing mapping file
    prefixFileName = geneListFileName[:-7]
    outputFile = open(prefixFileName+"mapping.txt","w")
    for e in geneList:
        for k in e[2].split(","):
            outputFile.write("\t".join([e[0],k])+"\n")
    outputFile.close()

    # Writing format file
    outputFile = open(prefixFileName+"preformat.txt","w")
    for e in geneList:
        outputFile.write(e[1]+"\n")
        for k in e[2].split(","):
            outputFile.write(k+"\n")
    outputFile.close()

    # Remove duplicates from format file
    os.system("sort "+prefixFileName+"preformat.txt | uniq > "+prefixFileName+"format.txt")
    os.system("rm "+prefixFileName+"preformat.txt")


