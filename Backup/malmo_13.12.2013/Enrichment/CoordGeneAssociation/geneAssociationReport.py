###################################################################################################
# Creates a report on gene-coordinate associations. It outputs a table (geneAssociationReport.txt) 
# that tells which genes where associated with at least one coordinate for every condition.
###################################################################################################

# Import
import os
import sys

# Input
geneListLoc = "/hpcwork/izkf/projects/malmo/Enrichment/GeneLists/"
inputFileList = [ "/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/all_genes_format/isletd_islets_diff_cut_20_format.bed",
                "/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/all_genes_format/islets_isletd_diff_cut_20_format.bed",
                "/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/coexpressed_genes_format/isletd_islets_diff_cut_20_format.bed",
                "/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/coexpressed_genes_format/islets_isletd_diff_cut_20_format.bed"
]

# Iterate on input file list
for inputFileName in inputFileList:
    
    # Read gene list
    geneFileName = geneListLoc+inputFileName.split("/")[7]+".txt"
    geneFile = open(geneFileName,"r")
    geneDict = dict()
    for line in geneFile:
        geneDict[line.strip()] = "FALSE"
    geneFile.close()
    geneList = geneDict.keys()

    # Iterating on inputFile
    inputFile = open(inputFileName,"r")
    for line in inputFile:
        ll = line.strip().split("\t")
        for g in ll[3].split(":"):
            if(g.split("_")[0] in geneList): geneDict[g.split("_")[0]] = "TRUE"
                
    # Writing dictionary
    outputFile = open(inputFileName[:-4]+"_report.txt","w")
    for g in geneList: outputFile.write("\t".join([g,geneDict[g]])+"\n")
        
    # Closing files
    inputFile.close()
    outputFile.close()


