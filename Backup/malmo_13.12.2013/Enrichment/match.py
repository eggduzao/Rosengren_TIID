
# Import
import os
import sys
import glob
from operator import itemgetter

# Input
tfMappingFileName = "/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/TF_mapping.txt"
geneFileNameList = [
                     "/hpcwork/izkf/projects/malmo/Enrichment/GeneLists/all_genes_format.txt",
                     "/hpcwork/izkf/projects/malmo/Enrichment/GeneLists/all_genes_format.txt",
                     "/hpcwork/izkf/projects/malmo/Enrichment/GeneLists/coexpressed_genes_format.txt",
                     "/hpcwork/izkf/projects/malmo/Enrichment/GeneLists/coexpressed_genes_format.txt",
                     "/hpcwork/izkf/projects/malmo/OLD/sox5_enrichment/CoordGeneAssociation/candidate_genes_format.txt", # OLD
                     "/hpcwork/izkf/projects/malmo/OLD/sox5_enrichment/CoordGeneAssociation/candidate_genes_format.txt" # OLD
]
inputFolderList = [
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/all_genes_format/isletd_islets_diff_cut_20/",
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/all_genes_format/islets_isletd_diff_cut_20/",
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/coexpressed_genes_format/isletd_islets_diff_cut_20/",
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/coexpressed_genes_format/islets_isletd_diff_cut_20/",
                    "/hpcwork/izkf/projects/malmo/OLD/sox5_enrichment/Results3/ds/", # OLD
                    "/hpcwork/izkf/projects/malmo/OLD/sox5_enrichment/Results3/sd/"  # OLD
]
inputFileList = [
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/all_genes_format/isletd_islets_diff_cut_20/MPBS_sox5.bed",
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/all_genes_format/islets_isletd_diff_cut_20/MPBS_sox5.bed",
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/all_genes_format/isletd_islets_diff_cut_20/MPBS_sox5.bed",
                    "/hpcwork/izkf/projects/malmo/Enrichment/Results/all_genes_format/islets_isletd_diff_cut_20/MPBS_sox5.bed",
                    "/hpcwork/izkf/projects/malmo/OLD/sox5_enrichment/Results3/ds/MPBS_sox5.bed", # OLD
                    "/hpcwork/izkf/projects/malmo/OLD/sox5_enrichment/Results3/sd/MPBS_sox5.bed"  # OLD
]

# Iterate on input folders
for i in range(0,len(inputFolderList)):

    # Initializations
    inputFolder = inputFolderList[i]
    geneFileName = geneFileNameList[i]
    inputFileName = inputFileList[i]

    # Read gene list (in order to keep in these files only the ones in the list)
    goldGeneList = []
    geneFile = open(geneFileName,"r")
    for line in geneFile:
        goldGeneList.append(line.strip())
    geneFile.close()

    # Reading MPBS_sox5.bed
    mpbsList = []
    inputFile = open(inputFileName,"r")
    for line in inputFile:
        ll = line.strip().split("\t")
        lll = ll[3].split(",")
        tfId1 = lll[0].upper()
        tfId2 = ""
        if("::" in tfId1): tfId2 = tfId1.split("::")[1]
        tfName = lll[1].upper()
        mpbsList.append(tfId1+","+tfId2+","+tfName)
    inputFile.close()

    # Removing duplicates
    mpbsList = list(set(mpbsList))

    # 3. Fetching all motifs around sox5
    outFile = open(inputFolder+"TF_sox5_all.txt","w")
    outFile.write("\t".join(["TF_ID","TF_NAME"])+"\n")
    for e in mpbsList:
        ee = e.split(",")
        tfId1 = ee[0]
        tfId2 = ee[1]
        tfName = ee[2]
        outFile.write("\t".join([tfId1,tfName])+"\n")
    outFile.close()

    # 2. Fetching motifs around sox5 that are inside the gene list
    outFile = open(inputFolder+"TF_sox5_genelist.txt","w")
    outFile.write("\t".join(["TF_ID","TF_NAME"])+"\n")
    for e in mpbsList:
        ee = e.split(",")
        tfId1 = ee[0]
        tfId2 = ee[1]
        tfName = ee[2]
        if((tfId2 in goldGeneList) or (tfName in goldGeneList)):
            outFile.write("\t".join([tfId1,tfName])+"\n")
    outFile.close()


