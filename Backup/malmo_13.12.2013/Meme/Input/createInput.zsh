#!/bin/zsh

# Parameters
inLoc="/hpcwork/izkf/projects/malmo/sox5_enrichment/Coordinates/"
outLoc="/hpcwork/izkf/projects/malmo/meme/Input/"
genome="/hpcwork/izkf/projects/egg/Data/HG19/hg19.fa"
inList=( "isletd_islets_diff_cut_20.bed" "islets_isletd_diff_cut_20.bed" )

# Loop
for inFile in $inList
do
    fastaFromBed -fi $genome -bed $inLoc$inFile -fo $outLoc$inFile
done

