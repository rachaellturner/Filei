source("http://www.bioconductor.org/biocLite.R")
biocLite("ggtree")

#loading packages.
library("ape")
library("Biostrings")
library("ggplot2")
library("ggtree")

#opening Newick format files for each ORF.
ENVtree <- read.tree("ENV_treefile")
POLtree <- read.tree("POL_treefile")
GAGtree <- read.tree("GAG_treefile")
ORF1tree <- read.tree("ORF1_treefile.txt")
ORF2tree <- read.tree("ORF2_treefile.txt")
ORF0tree <- read.tree("ORF0_treefile.txt")

#plotting phylogenetic tree for each ORF.
ENV <- ggtree(ENVtree) + geom_tiplab(size = 4, colour = "blue") + geom_treescale()
POL <- ggtree(POLtree) + geom_tiplab(size = 4, colour = "blue") + geom_treescale()
GAG <- ggtree(GAGtree) + geom_tiplab(size = 4, colour = "blue") + geom_treescale()

ORF1 <- ggtree(ORF1tree) + geom_tiplab(size = 4, colour = "blue") + geom_treescale()
ORF2 <- ggtree(ORF2tree) + geom_tiplab(size = 4, colour = "blue") + geom_treescale()
ORF0 <- ggtree(ORF0tree) + geom_tiplab(size = 4, colour = "blue") + geom_treescale()

#printing each plot.
ENV
POL
GAG
ORF1
ORF2
ORF0
