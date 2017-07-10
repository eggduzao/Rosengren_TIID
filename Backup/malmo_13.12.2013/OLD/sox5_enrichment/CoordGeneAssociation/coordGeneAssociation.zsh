#!/bin/zsh

# Global Parameters
gene_list="-gene_list=/hpcwork/izkf/projects/malmo/sox5_enrichment/CoordGeneAssociation/candidate_genes_format.txt"
organism="-organism=hg19"
promoter_length="-promoter_length=1000"
maximum_association_length="-maximum_association_length=50000"
print_association="-print_association=Y"
print_mpbs="-print_mpbs=N"
print_results_text="-print_results_text=N"
print_results_html="-print_results_html=N"
print_enriched_genes="-print_enriched_genes=N"
print_rand_coordinates="-print_rand_coordinates=N"
print_graph_mmscore="-print_graph_mmscore=N"

# DS
coord_file="-coord_file=/hpcwork/izkf/projects/malmo/sox5_enrichment/Coordinates/isletd_islets_diff_cut_20.bed"
outLoc="/hpcwork/izkf/projects/malmo/sox5_enrichment/CoordGeneAssociation/ds/"
output_location="-output_location="$outLoc
mkdir -p $outLoc
rgt-motifanalysis enrichment $coord_file $gene_list $organism $promoter_length $maximum_association_length $output_location $print_association $print_mpbs $print_results_text $print_results_html $print_enriched_genes $print_rand_coordinates $print_graph_mmscore

# SD
coord_file="-coord_file=/hpcwork/izkf/projects/malmo/sox5_enrichment/Coordinates/islets_isletd_diff_cut_20.bed"
outLoc="/hpcwork/izkf/projects/malmo/sox5_enrichment/CoordGeneAssociation/sd/"
output_location="-output_location="$outLoc
mkdir -p $outLoc
rgt-motifanalysis enrichment $coord_file $gene_list $organism $promoter_length $maximum_association_length $output_location $print_association $print_mpbs $print_results_text $print_results_html $print_enriched_genes $print_rand_coordinates $print_graph_mmscore


