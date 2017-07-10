#!/bin/zsh

# Input
asocFileName="/hpcwork/izkf/projects/malmo/CoordGeneAssociation/association_file_upper.bed" 
geneLoc="/hpcwork/izkf/projects/malmo/GeneLists/"
outLoc="/hpcwork/izkf/projects/malmo/PromoterRegions/"
geneLists=( "all_genes" "coexpressed_genes" )

# Execution
for g in $geneLists
do
  python fetchPromoterBackground.py $geneLoc$g"_format.txt" $asocFileName $outLoc$g"_promoter_back_500.bed"
done


