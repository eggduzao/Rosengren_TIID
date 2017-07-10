#!/bin/zsh

ds="/hpcwork/izkf/projects/malmo/Motif_Matching/Input/isletd_islets_diff_cut_20.bed"
sd="/hpcwork/izkf/projects/malmo/Motif_Matching/Input/islets_isletd_diff_cut_20.bed"
sox="/hpcwork/izkf/projects/malmo/Motif_Matching/Input/sox5_region.bed"

intersectBed -a $ds -b $sox -wa > "ds.bed"
intersectBed -a $sd -b $sox -wa > "sd.bed"


