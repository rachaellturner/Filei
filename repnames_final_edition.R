testdf2 <- read.csv("/Users/mehitabelowusu/Downloads/L1M1_positions.csv")

start_function_test <- function(chr) {
  numbers <- which(testdf2[,5] == chr)
  start <- testdf2$genoStart[numbers]
  return(start)
}

end_function_test <- function(chr) {
  numbers <- which(testdf2[,5] == chr)
  end <- testdf2$genoEnd[numbers]
  return(end)
}

CHR1s <- start_function_test("chr1")
CHR1e <- end_function_test("chr1")

CHR2s<-start_function_test("chr2")
CHR2e<-end_function_test("chr2")

CHR3s<-start_function_test("chr3")
CHR3e<-end_function_test("chr3")

CHR4s<-start_function_test("chr4")
CHR4e<-end_function_test("chr4")

CHR5s<-start_function_test("chr5")
CHR5e<-end_function_test("chr5")

CHR6s<-start_function_test("chr6")
CHR6e<-end_function_test("chr6")

CHR7s<-start_function_test("chr7")
CHR7e<-end_function_test("chr7")

CHR8s<-start_function_test("chr8")
CHR8e<-end_function_test("chr8")

CHR9s<-start_function_test("chr9")
CHR9e<-end_function_test("chr9")

CHR10s<-start_function_test("chr10")
CHR10e<-end_function_test("chr10")

CHR11s<-start_function_test("chr11")
CHR11e<-end_function_test("chr11")

CHR12s<-start_function_test("chr12")
CHR12e<-end_function_test("chr12")

CHR13s<-start_function_test("chr13")
CHR13e<-end_function_test("chr13")

CHR14s<-start_function_test("chr14")
CHR14e<-end_function_test("chr14")

CHR15s<-start_function_test("chr15")
CHR15e<-end_function_test("chr15")

CHR16s<-start_function_test("chr16")
CHR16e<-end_function_test("chr16")

CHR17s<-start_function_test("chr17")
CHR17e<-end_function_test("chr17")

CHR18s<-start_function_test("chr18")
CHR18e<-end_function_test("chr18")

CHR19s<-start_function_test("chr19")
CHR19e<-end_function_test("chr19")

CHR20s<-start_function_test("chr20")
CHR20e<-end_function_test("chr20")

CHR21s<-start_function_test("chr21")
CHR21e<-end_function_test("chr21")

CHR22s<-start_function_test("chr22")
CHR22e<-end_function_test("chr22")

CHRXs<-start_function_test("chrX")
CHRXe<-end_function_test("chrX")

CHRYs<-start_function_test("chrY")
CHRYe<-end_function_test("chrY")

source("https://bioconductor.org/biocLite.R")
biocLite("karyoploteR")
library(karyoploteR)

regionchr1<-makeGRangesFromDataFrame(data.frame(chr=c("chr1"), start=CHR1s, end=CHR1e))
regionchr2<-makeGRangesFromDataFrame(data.frame(chr=c("chr2"), start=CHR2s, end=CHR2e))
regionchr3<-makeGRangesFromDataFrame(data.frame(chr=c("chr3"), start=CHR3s, end=CHR3e))
regionchr4<-makeGRangesFromDataFrame(data.frame(chr=c("chr4"), start=CHR4s, end=CHR4e))
regionchr5<-makeGRangesFromDataFrame(data.frame(chr=c("chr5"), start=CHR5s, end=CHR5e))
regionchr6<-makeGRangesFromDataFrame(data.frame(chr=c("chr6"), start=CHR6s, end=CHR6e))
regionchr7<-makeGRangesFromDataFrame(data.frame(chr=c("chr7"), start=CHR7s, end=CHR7e))
regionchr8<-makeGRangesFromDataFrame(data.frame(chr=c("chr8"), start=CHR8s, end=CHR8e))
regionchr9<-makeGRangesFromDataFrame(data.frame(chr=c("chr9"), start=CHR9s, end=CHR9e))
regionchr10<-makeGRangesFromDataFrame(data.frame(chr=c("chr10"), start=CHR10s, end=CHR10e))
regionchr11<-makeGRangesFromDataFrame(data.frame(chr=c("chr11"), start=CHR11s, end=CHR11e))
regionchr12<-makeGRangesFromDataFrame(data.frame(chr=c("chr12"), start=CHR12s, end=CHR12e))
regionchr13<-makeGRangesFromDataFrame(data.frame(chr=c("chr13"), start=CHR13s, end=CHR13e))
regionchr14<-makeGRangesFromDataFrame(data.frame(chr=c("chr14"), start=CHR14s, end=CHR14e))
regionchr15<-makeGRangesFromDataFrame(data.frame(chr=c("chr15"), start=CHR15s, end=CHR15e))
regionchr16<-makeGRangesFromDataFrame(data.frame(chr=c("chr16"), start=CHR16s, end=CHR16e))
regionchr17<-makeGRangesFromDataFrame(data.frame(chr=c("chr17"), start=CHR17s, end=CHR17e))
regionchr18<-makeGRangesFromDataFrame(data.frame(chr=c("chr18"), start=CHR18s, end=CHR18e))
regionchr19<-makeGRangesFromDataFrame(data.frame(chr=c("chr19"), start=CHR19s, end=CHR19e))
regionchr20<-makeGRangesFromDataFrame(data.frame(chr=c("chr20"), start=CHR20s, end=CHR20e))
regionchr21<-makeGRangesFromDataFrame(data.frame(chr=c("chr21"), start=CHR21s, end=CHR21e))
regionchr22<-makeGRangesFromDataFrame(data.frame(chr=c("chr22"), start=CHR22s, end=CHR22e))
regionchrX<-makeGRangesFromDataFrame(data.frame(chr=c("chrX"), start=CHRXs, end=CHRXe))
regionchrY<-makeGRangesFromDataFrame(data.frame(chr=c("chrY"), start=CHRYs, end=CHRYe))

kp<-plotKaryotype(genome = "hg38")


kpPlotRegions(kp, regionchr1, col = "#AA88FF")
kpPlotRegions(kp, regionchr2, col = "#AA88FF")
kpPlotRegions(kp, regionchr3, col = "#AA88FF")
kpPlotRegions(kp, regionchr4, col = "#AA88FF")
kpPlotRegions(kp, regionchr5, col = "#AA88FF")
kpPlotRegions(kp, regionchr6, col = "#AA88FF")
kpPlotRegions(kp, regionchr7, col = "#AA88FF")
kpPlotRegions(kp, regionchr8, col = "#AA88FF")
kpPlotRegions(kp, regionchr9, col = "#AA88FF")
kpPlotRegions(kp, regionchr10, col = "#AA88FF")
kpPlotRegions(kp, regionchr11, col = "#AA88FF")
kpPlotRegions(kp, regionchr12, col = "#AA88FF")
kpPlotRegions(kp, regionchr13, col = "#AA88FF")
kpPlotRegions(kp, regionchr14, col = "#AA88FF")
kpPlotRegions(kp, regionchr15, col = "#AA88FF")
kpPlotRegions(kp, regionchr16, col = "#AA88FF")
kpPlotRegions(kp, regionchr17, col = "#AA88FF")
kpPlotRegions(kp, regionchr18, col = "#AA88FF")
kpPlotRegions(kp, regionchr19, col = "#AA88FF")
kpPlotRegions(kp, regionchr20, col = "#AA88FF")
kpPlotRegions(kp, regionchr21, col = "#AA88FF")
kpPlotRegions(kp, regionchr22, col = "#AA88FF")
kpPlotRegions(kp, regionchrX, col = "#AA88FF")
kpPlotRegions(kp, regionchrY, col = "#AA88FF")