from rpy2.robjects.packages import importr

def run():
    packnames = ['ggplot2','GenomicRanges','ggbio','IRanges','karyoploteR','mzID','Biostrings','msa','ggseqlogo']
    
    base = importr('base')

    base.source("http://www.bioconductor.org/biocLite.R")

    biocinstaller = importr("BiocInstaller")
    
    for package in packnames:
        biocinstaller.biocLite(package)
