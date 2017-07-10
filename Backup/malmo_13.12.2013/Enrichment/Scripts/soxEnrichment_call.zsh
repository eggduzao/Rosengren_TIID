#!/bin/zsh

##########################################################################
### Motif Enrichment Analysis for DNase enriched regions in human islets
### Input files are coordinates associated with genes from gene list.
##########################################################################

# Global Parameters
inputLoc="/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/"
outputLoc="/hpcwork/izkf/projects/malmo/Enrichment/Results/"

# Gene Parameters
geneList=( "all_genes_format" "coexpressed_genes_format" )

# Gene Loop
for geneFile in $geneList
do

    # Coordinate Parameters
    coordList=( "isletd_islets_diff_cut_20" "islets_isletd_diff_cut_20" )

    # Coordinate Loop
    for coordFile in $coordList
    do

        # Parameters
        assoc_coord_file="-assoc_coord_file="$inputLoc$geneFile"/"$coordFile"_format.bed" # Coordinate already associated with genes
        logo_location="-logo_location=../../logo/"
        organism="-organism=hg19"
        motif_match_fpr="-motif_match_fpr=0.0001"
        motif_match_precision="-motif_match_precision=10000"
        motif_match_pseudocounts="-motif_match_pseudocounts=0.05"
        multiple_test_alpha="-multiple_test_alpha=0.05"
        promoter_length="-promoter_length=1000"
        maximum_association_length="-maximum_association_length=50000"
        rand_proportion_size="-rand_proportion_size=3.0"
        outputLocation=$outputLoc$geneFile"/"$coordFile"/"
        output_location="-output_location="$outputLocation
        print_association="-print_association=Y"
        print_mpbs="-print_mpbs=Y"
        print_results_text="-print_results_text=Y"
        print_results_html="-print_results_html=Y"
        print_enriched_genes="-print_enriched_genes=N"
        print_rand_coordinates="-print_rand_coordinates=Y"
        print_graph_mmscore="-print_graph_mmscore=N"

        # Execution
        mkdir -p $outputLocation
        bsub -J $geneFile"_"$coordFile"_ME" -o $geneFile"_"$coordFile"_ME_out.txt" -e $geneFile"_"$coordFile"_ME_err.txt" -W 200:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifStatistics_pipeline.zsh $assoc_coord_file $logo_location $organism $motif_match_fpr $motif_match_precision $motif_match_pseudocounts $multiple_test_alpha $promoter_length $maximum_association_length $rand_proportion_size $output_location $print_association $print_mpbs $print_results_text $print_results_html $print_enriched_genes $print_rand_coordinates $print_graph_mmscore

    done
done


