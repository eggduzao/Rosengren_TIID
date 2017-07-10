#!/bin/zsh

##########################################################################
### Motif Enrichment Analysis for DNase enriched regions in human islets
### Input files are coordinates associated with genes from gene list.
##########################################################################

# Global Parameters
logo_location="-logo_location=../../logo/"
organism="-organism=hg19"
motif_match_fpr="-motif_match_fpr=0.0001"
motif_match_precision="-motif_match_precision=10000"
motif_match_pseudocounts="-motif_match_pseudocounts=0.05"
multiple_test_alpha="-multiple_test_alpha=0.05"
promoter_length="-promoter_length=1000"
maximum_association_length="-maximum_association_length=50000"
rand_proportion_size="-rand_proportion_size=3.0"
print_association="-print_association=Y"
print_mpbs="-print_mpbs=Y"
print_results_text="-print_results_text=Y"
print_results_html="-print_results_html=Y"
print_enriched_genes="-print_enriched_genes=N"
print_rand_coordinates="-print_rand_coordinates=Y"
print_graph_mmscore="-print_graph_mmscore=N"
outLoc="/hpcwork/izkf/projects/malmo/sox5_enrichment/Results3/"

# Coordinate Parameters
cl="/hpcwork/izkf/projects/malmo/sox5_enrichment/CoordGeneAssociation/"
coordList=( "ds" "sd" )

# Coordinate Loop
for coordFile in $coordList
do

    # Parameters
    assoc_coord_file="-assoc_coord_file="$cl$coordFile".bed" # Coordinate already associated with genes
    outputLocation=$outLoc$coordFile"/"
    output_location="-output_location="$outputLocation # Output
    mkdir -p $outputLocation

    # Execution
    bsub -J $coordFile"_SOXME3" -o $coordFile"_SOXME3_out.txt" -e $coordFile"_SOXME3_err.txt" -W 200:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifStatistics_pipeline2.zsh $assoc_coord_file $logo_location $organism $motif_match_fpr $motif_match_precision $motif_match_pseudocounts $multiple_test_alpha $promoter_length $maximum_association_length $rand_proportion_size $output_location $print_association $print_mpbs $print_results_text $print_results_html $print_enriched_genes $print_rand_coordinates $print_graph_mmscore

done

# 


