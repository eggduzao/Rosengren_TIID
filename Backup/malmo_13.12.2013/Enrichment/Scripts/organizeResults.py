###################################################################################################
# Organizes the Results in Malmo project for Sonja.
###################################################################################################
# 1. Remove nev results.
# 2. Rename rand files.
###################################################################################################
# 3. File TF_all.txt
#    Full list of transcription factors that had at least one occurence inside coordinates
#    associated with genes on gene list. This list contains the following columns:
#    TF ID, Name of TF, Corrected p-value, p-value, gene list. It is ordered by corrected p-value and then 
#    p-value and then lexically by the name of the TF. The name of the TF is obtained by
#    mapping the ID to the TF's gene name with TF_mapping.txt. If the TF ID is not mappable it will present a NA instead.
# 4. File TF_enriched.txt
#    Same list as above, but with factors that had p-value smaller than or equal 0.05.
###################################################################################################
# 5. File MPBS_all.bed
#    All MPBSs inside the coordinates associated with genes (green entries). The bed file has these fields:
#    Chromosome, Pos1 of TF, Pos2 of TF, <TF_ID><,><Gene list separated by colon>, MM bitscore [0,1000], strand of TF.
# 6. File MPBS_enriched.bed
#    Extract MPBSs from enriched factors inside the coordinates associated with genes (green entries).
#    The bed has the same fields as above.
# 7. File MPBS_sox5.bed
#    Extract all motifs around coordinates associated with sox5 (green entries). The bed has the same fields as above
#    with the exception of the NAME field, which does not contain the gene name (since it is all sox5). Instead,
#    it contains the TF name (or NA if non existing).
###################################################################################################

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
enrichPvalue = 0.05

# Reading TF mapping
tfDict = dict()
tfFile = open(tfMappingFileName,"r")
tfFile.readline()
for line in tfFile:
    ll = line.strip().split("\t")
    tfDict[ll[1]] = ll[4].upper()
tfFile.close()

# Iterate on input folders
for i in range(0,len(inputFolderList)):

    # Initializations
    inputFolder = inputFolderList[i]
    geneFileName = geneFileNameList[i]

    # Read gene list (in order to keep in these files only the ones in the list)
    # This is necessary because a coordinate can be mapped to two genes and a gene outside the list
    # can appear if this coordinate is associated with one gene in the list.
    goldGeneList = []
    geneFile = open(geneFileName,"r")
    for line in geneFile:
        goldGeneList.append(line.strip())
    geneFile.close()

    # 1. Remove nev results #######################################################################
    for e in glob.glob(inputFolder+"nev_*"): os.system("rm "+e)

    # 2. Rename all files #########################################################################
    renameList = [["rand_1_statistics.html","statistics.html"],["rand_1_statistics.txt","statistics.txt"]]
    for r in renameList:
        if(os.path.exists(inputFolder+r[0])): os.system("mv "+inputFolder+r[0]+" "+inputFolder+r[1])

    # 3. File TFs_all.txt #########################################################################
    # 4. File TFs enriched.txt ####################################################################

    # Get TF table
    tfTable = []
    inputFile = open(inputFolder+"statistics.txt","r")
    inputFile.readline()
    for line in inputFile:
        ll = line.strip().split("\t")
        if(float(ll[3]) >= 1.0): # Get only the TFs that had at least one hit in coordinates that were associated with genes on gene list
            oldGeneList = ll[9].split(",")
            newGeneList = [e for e in oldGeneList if e in goldGeneList]
            try:
                tfTable.append([ll[0],tfDict[ll[0]],float(ll[2]),float(ll[1]),",".join(newGeneList)])
            except KeyError:
                tfTable.append([ll[0],"NA",float(ll[2]),float(ll[1]),",".join(newGeneList)])
    inputFile.close()

    # Sort table
    tfTable = sorted(tfTable, key=itemgetter(2,3,0))

    # Write all TFs
    outputFile = open(inputFolder+"TF_all.txt","w")
    outputFile.write("\t".join(["FACTOR_ID","FACTOR_NAME","CORR_PVALUE","PVALUE","GENES"])+"\n")
    for e in tfTable:
        outputFile.write("\t".join([str(k) for k in e])+"\n")
    outputFile.close()

    # Write enriched TFs
    outputFile = open(inputFolder+"TF_enriched.txt","w")
    outputFile.write("\t".join(["FACTOR_ID","FACTOR_NAME","CORR_PVALUE","PVALUE","GENES"])+"\n")
    for e in tfTable:
        if(e[2] <= enrichPvalue): outputFile.write("\t".join([str(k) for k in e])+"\n")
    outputFile.close()

    # 5. File MPBS_all.bed ########################################################################
    # 6. File MPBS_enriched.bed ###################################################################
    # 7. File MPBS_sox5.bed #######################################################################
    
    # Converting bigbed to bed
    toDelete = [inputFolder+"mpbs.bed",inputFolder+"coord_association.bed"]
    os.system("bigBedToBed "+inputFolder+"mpbs.bb "+inputFolder+"mpbs.bed")
    os.system("bigBedToBed "+inputFolder+"coord_association.bb "+inputFolder+"coord_association.bed")

    # Itersecting mpbs with gene-coordinate association
    os.system("intersectBed -wa -wb -a "+inputFolder+"coord_association.bed -b "+inputFolder+"mpbs.bed > "+inputFolder+"TEMP_INTERSECTION.bed")
    toDelete.append(inputFolder+"TEMP_INTERSECTION.bed")

    # Reading intersection file
    inputFile = open(inputFolder+"TEMP_INTERSECTION.bed","r")
    mpbsTable = []
    mpbsTableNoGeneSox5 = []
    for line in inputFile:
        ll = line.strip().split("\t")
        newGeneList = ":".join([e for e in [k.split("_")[0] for k in ll[3].split(":")] if e in goldGeneList])
        if(len(newGeneList) > 0): newGeneList = "," + newGeneList
        mpbsTable.append([ll[9],ll[10],ll[11],ll[12]+newGeneList,ll[13],ll[14]])
        if(("SOX5_PROX" in ll[3].split(":")) or ("SOX5_DIST" in ll[3].split(":"))):
            try:
                mpbsTableNoGeneSox5.append([ll[9],ll[10],ll[11],ll[12]+","+tfDict[ll[12]],ll[13],ll[14]])
            except KeyError:
                mpbsTableNoGeneSox5.append([ll[9],ll[10],ll[11],ll[12]+",NA",ll[13],ll[14]])
    inputFile.close()

    # Writting all MPBSs
    outputFile = open(inputFolder+"MPBS_all.bed","w")
    for e in mpbsTable:
        outputFile.write("\t".join([str(k) for k in e])+"\n")
    outputFile.close()
    
    # Writting MPBSs of enriched TFs only
    enrichedTable = [e[0] for e in tfTable if e[2] <= enrichPvalue]
    outputFile = open(inputFolder+"MPBS_enriched.bed","w")
    for e in mpbsTable:
        if(e[3].split(",")[0] in enrichedTable): outputFile.write("\t".join([str(k) for k in e])+"\n")
    outputFile.close()

    # Writting all MPBSs in coordinates associated with sox5
    outputFile = open(inputFolder+"MPBS_sox5.bed","w")
    for e in mpbsTableNoGeneSox5:
        outputFile.write("\t".join([str(k) for k in e])+"\n")
    outputFile.close()

    # Removing files
    for e in toDelete: os.system("rm "+e)


