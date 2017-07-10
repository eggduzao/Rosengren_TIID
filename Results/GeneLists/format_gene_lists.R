
candidate_genes = read.table("candidate_genes.txt", sep = "\t", header = F)
#assoc_file = read.table("association_file.bed", sep = "\t", header = F)

candidate_genes$V1 = toupper(candidate_genes$V1)
#not_in_assoc_file = setdiff(candidate_genes$V1, toupper(assoc_file$V4))

candidate_genes$V1[candidate_genes$V1 == "C9ORF150"] = "LURAP1L"
candidate_genes$V1[candidate_genes$V1 == "FAM123C"] = "AMER3"
candidate_genes$V1[candidate_genes$V1 == "FAM148A"] = "C2CD4A"
candidate_genes$V1[candidate_genes$V1 == "KIAA0774"] = "MTUS2"
candidate_genes$V1[candidate_genes$V1 == "KIAA1383"] = "MAP10"
candidate_genes$V1[candidate_genes$V1 == "KIAA1486"] = "NYAP2"
candidate_genes$V1[candidate_genes$V1 == "BRAC"] = "T"
candidate_genes$V1[candidate_genes$V1 == "ODZ3"] = "TENM3"
candidate_genes$V1[candidate_genes$V1 == "BAPX1"] = "NKX3-2"
candidate_genes$V1[candidate_genes$V1 == "CEBP"] = "CPEB1"
candidate_genes$V1[candidate_genes$V1 == "DELTAEF1"] = "ZEB2"

#intersect(candidate_genes$V1, toupper(assoc_file$V4))

write.table(toupper(candidate_genes$V1),file = "candidate_genes_format.txt", sep = "\t", col.names = F, row.names = F, quote = F)

######################################################################################

candidate_genes = read.table("co_expressed_genes.txt", sep = "\t", header = F)
#assoc_file = read.table("association_file.bed", sep = "\t", header = F)

candidate_genes$V1 = toupper(candidate_genes$V1)
#not_in_assoc_file = setdiff(candidate_genes$V1, toupper(assoc_file$V4))

candidate_genes$V1[candidate_genes$V1 == "C9ORF150"] = "LURAP1L"

#intersect(candidate_genes$V1, toupper(assoc_file$V4))

write.table(toupper(candidate_genes$V1),file = "co_expressed_genes_format.txt", sep = "\t", col.names = F, row.names = F, quote = F)





