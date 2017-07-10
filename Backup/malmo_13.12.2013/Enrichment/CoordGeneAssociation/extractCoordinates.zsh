#!/bin/zsh

# Global Parameters
l="/hpcwork/izkf/projects/malmo/Enrichment/CoordGeneAssociation/"

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

        grep 0,130,0 $l$geneFile"/"$coordFile".bed" > $l$geneFile"/"$coordFile"_format.bed"

    done
done


