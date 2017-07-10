
grep "0\,130\,0" FOXP2_coexpressed_genes_promoter_500.bed | mergeBed -d 100 -i stdin > FOXP2_coexpressed_genes_promoter_merged.bed
grep "0\,130\,0" BARX2_coexpressed_genes_promoter_500.bed | mergeBed -d 100 -i stdin > BARX2_coexpressed_genes_promoter_merged.bed
grep "0\,130\,0" NKX6-1_coexpressed_genes_promoter_500.bed | mergeBed -d 100  -i stdin > NKX6-1_coexpressed_genes_promoter_merged.bed
grep "0\,130\,0" PDX1_coexpressed_genes_promoter_500.bed | mergeBed -d 100 -i stdin > PDX1_coexpressed_genes_promoter_merged.bed
grep "0\,130\,0" SOX5_coexpressed_genes_promoter_500.bed | mergeBed -d 100 -i stdin > SOX5_coexpressed_genes_promoter_merged.bed
