
###################################################################################################
###################################################################################################
##### MALMO PROJECT
# This is the readme for the malmo project. It contains log information on the files
# created/modified by EG, SH and IC.
###################################################################################################
###################################################################################################

##### Enrichment ##################################################################################
# This folder contains the enrichment analysis made on:
# Gene Lists: all_genes_format.txt and coexpressed_genes_format.txt
# Coordinate Sets: isletd_islets_diff_cut_20.bed & islets_isletd_diff_cut_20.bed

# CoordGeneAssociation
- Order of script usage:
  1. coordGeneAssociation.zsh (source code need to be modified in order to run only the association)
  2. extractCoordinates.zsh
  3. geneAssociationReport.py
- all_genes_format: This forder represents the coordinate-gene associations based on
  the all_genes_format.txt gene list.
  - isletd_islets_diff_cut_20.bed & islets_isletd_diff_cut_20.bed: Files generated with coordGeneAssociation.zsh
    based on the input coordinates with the same name on the Coordinates folder. These files contain the association
    of ALL coordinates with ALL genes. The coordinates associated with genes on the all_genes_format.txt list are 
    in green, coordinates associated with genes outside the list are in red and non-associated coordinates are in black.
  - isletd_islets_diff_cut_20_format.bed & islets_isletd_diff_cut_20_format.bed: Files generated with extractCoordinate.zsh
    representing only the green entries (coordinates associated with genes on all_genes_format.txt) of the non-format versions
    on the same folder.
  - unknownGenes.txt: Genes that were on the all_genes_raw.txt list but were not found in association_file.bed and could
    not be mapped using uniprot website.
- coexpressed_genes_format: This folder represents the coordinate-gene associations based on
  the coexpressed_genes_format.txt gene list. It contains the same contents as all_genes_format.
- association_file.bed: Contains the gene locations. It is the same file that is used by RGT.
- association_file_upper.bed: Same file as above but with all genes CAPS.
- coordGeneAssociation.zsh: Script to associate the coordinates with gene-lists given the association
  file association_file_upper.bed (it uses RGT, which needs to be modified in order to run only the association).
- extractCoordinates.zsh: Script to extract the coordinates associated with genes on gene lists (green entries).

# Coordinates
- isletd_islets_diff_cut_20.bed & islets_isletd_diff_cut_20.bed: Input DNase-seq coordinates. Peaks
  were downloaded from ENCODE and selected based on a cutoff of 20 (SH & IC). EG uses as main input
  coordinates for the enrichment operation.

# GeneLists
- all_genes_raw.txt: Raw version of all genes (1st analysis).
- coexpressed_genes_raw.txt & coexpressed_genes_raw.xls: Raw version of coexpressed genes (2nd analysis).
- all_genes_format.txt: Formatted version of all_genes_raw.txt by SH.
- coexpressed_genes_format.txt: Formatted version of coexpressed_genes_raw.txt by SH.

# Results
- all_genes_format: Results for all genes list.
  - isletd_islets_diff_cut_20 & islets_isletd_diff_cut_20: Results for these coordinate sets. Structure below:
    - # TODO
- coexpressed_genes_format: Results for coexpressed genes. Same structure as all_genes_format

# Scripts
- ClusterOutput: Contains the files outputted by the cluster (out and err).
- motifStatistics_pipeline.zsh: The (middle) script that calls the RGT within the cluster.
- separateEnrichedMotifs.py: #TODO
- soxEnrichment_call.zsh: The script that performs the cluster call to perform the motif enrichment.

##### Meme ########################################################################################
# This folder contains the meme analysis of the islet DNase-seq regions

# Input
- createInput.zsh: meme-chip takes as input a fasta file containing the DNA sequences of the regions
  to be analyzed. As we had a bed file containing the peaks (after significance
  threshold of 20 was applied), this script fetches the sequences by using fastaFromBed
  binary program (available on cluster) to extract the DNA sequences of the bed files
  from human genome HG19.
- isletd_islets_diff_cut_20.fa: Fasta file containing the sequences extracted from isletd_islets_diff_cut_20.bed
  using HG19 as reference.
- islets_isletd_diff_cut_20.fa: Fasta file containing the sequences extracted from islets_isletd_diff_cut_20.bed
  using HG19 as reference.

# Output
- IsletD_IsletS: Results after applying meme-chip on isletd_islets_diff_cut_20.fa.
- IsletS_IsletD: Results after applying meme-chip on islets_isletd_diff_cut_20.fa.
- The software meme-chip is available at: http://meme.nbcr.net/meme/cgi-bin/meme-chip.cgi
  these results correspond to the download of all applied tools.




