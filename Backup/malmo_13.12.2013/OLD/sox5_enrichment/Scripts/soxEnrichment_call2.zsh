#!/bin/zsh

##########################################################################
### Motif Enrichment Analysis for DNase enriched regions around Sox.
### Genes = All genes as enriched [not important because all coordinates will be ev file]
### Coordinates = Coordinates/
### TFs = All motifs in internal dataset [primary]
##########################################################################

# Global Parameters
logo_location="-logo_location=../../logo/"
organism="-organism=hg19"
multiple_test_alpha="-multiple_test_alpha=0.05"
promoter_length="-promoter_length=1000"
maximum_association_length="-maximum_association_length=50000"
rand_proportion_size="-rand_proportion_size=10.0"
all_coord_evidence="-all_coord_evidence=Y"
use_precomp_mm="-use_precomp_mm=Y"
print_association="-print_association=Y"
print_mpbs="-print_mpbs=Y"
print_results_text="-print_results_text=Y"
print_results_html="-print_results_html=Y"
print_enriched_genes="-print_enriched_genes=N"
print_rand_coordinates="-print_rand_coordinates=Y"
print_graph_mmscore="-print_graph_mmscore=N"
outLoc="/hpcwork/izkf/projects/malmo/sox5_enrichment/Results2/"

# Coordinate Parameters
cl="/hpcwork/izkf/projects/malmo/sox5_enrichment/Coordinates/"
coordList=( "isletd_islets_diff_cut_20" "islets_isletd_diff_cut_20" )

# Coordinate Loop
for coordFile in $coordList
do

    # Parameters
    coord_file="-coord_file="$cl$coordFile".bed" # Coordinate
    outputLocation=$outLoc$coordFile"/"
    output_location="-output_location="$outputLocation # Output
    mkdir -p $outputLocation

    # Execution
    bsub -J $coordFile"_SOXME2" -o $coordFile"_SOXME2_out.txt" -e $coordFile"_SOXME2_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifStatistics_pipeline2.zsh $coord_file $logo_location $organism $multiple_test_alpha $promoter_length $maximum_association_length $rand_proportion_size $all_coord_evidence $use_precomp_mm $output_location $print_association $print_mpbs $print_results_text $print_results_html $print_enriched_genes $print_rand_coordinates $print_graph_mmscore

done


