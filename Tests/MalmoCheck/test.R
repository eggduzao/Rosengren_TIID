


system("intersectBed -a Pancreatic_islets_dedifDukeDNaseSeq.bed -b Pancreatic_isletsDukeDNaseSeq.bed -v > isletd_islets_diff.bed")


#system("intersectBed -a wgEncodeAwgDnaseDukePanisletsUniPk.narrowPeak
#-b wgEncodeAwgDnaseDukePanisletdUniPk.narrowPeak -v >
#islets_isletd_diff.bed")


#system("cut -f1,2,3,7 isletd_islets_diff.bed > isletd_islets_diff_cut.bed")
#system("cut -f1,2,3,7 islets_isletd_diff.bed > islets_isletd_diff_cut.bed")


#islets = read.table("islets_isletd_diff_cut.bed")
#isletd = read.table("isletd_islets_diff_cut.bed")


#istletd2 = subset(isletd, V4 >= 20)

#write.table(istletd2, file = "isletd_islets_diff_cut_20.bed",
#row.names = F, col.names = F, quote = F)


#istlets2 = subset(islets, V4 >= 20)

#write.table(istlets2, file = "islets_isletd_diff_cut_20.bed",
#row.names = F, col.names = F, quote = F)
