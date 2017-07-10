#!/bin/zsh

# Gene Parameters
gl="/hpcwork/izkf/projects/malmo/Enrichment/GeneLists/"
geneList=( "all_genes_format" "coexpressed_genes_format" )

# Gene Loop
for geneFile in $geneList
do

    # Coordinate Parameters
    cl="/hpcwork/izkf/projects/malmo/Enrichment/Coordinates/"
    coordList=( "isletd_islets_diff_cut_20" "islets_isletd_diff_cut_20" )

    # Coordinate Loop
    for coordFile in $coordList
    do

        # Parameters
        coord_file="-coord_file="$cl$coordFile".bed"
        gene_list="-gene_list="$gl$geneFile".txt"
        association_file="-association_file=/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/association_file_upper.bed"
        organism="-organism=hg19"
        promoter_length="-promoter_length=1000"
        maximum_association_length="-maximum_association_length=50000"
        outputLocation="/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/"$geneFile"/"$coordFile"/"
        output_location="-output_location="$outputLocation
        print_association="-print_association=Y"
        print_mpbs="-print_mpbs=N"
        print_results_text="-print_results_text=N"
        print_results_html="-print_results_html=N"
        print_enriched_genes="-print_enriched_genes=N"
        print_rand_coordinates="-print_rand_coordinates=N"
        print_graph_mmscore="-print_graph_mmscore=N"

        # Execution
        mkdir -p $outputLocation
        rgt-motifanalysis enrichment $coord_file $gene_list $association_file $organism $promoter_length $maximum_association_length $output_location $print_association $print_mpbs $print_results_text $print_results_html $print_enriched_genes $print_rand_coordinates $print_graph_mmscore
        bigBedToBed $outputLocation"coord_association.bb" $outputLocation"coord_association.bed"
        mv $outputLocation"coord_association.bed" "/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/"$geneFile"/"$coordFile".bed"
        rm -rf $outputLocation

    done
done


