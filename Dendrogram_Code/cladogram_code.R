source("http://www.bioconductor.org/biocLite.R")
biocLite("ggtree")

library("ape")
library("Biostrings")
library("ggplot2")
library("ggtree")

ENVtree <- read.tree("ENV_treefile")
POLtree <- read.tree("POL_treefile")
GAGtree <- read.tree("GAG_treefile")
ORF1tree <- read.tree("ORF1_treefile.txt")
ORF2tree <- read.tree("ORF2_treefile.txt")
ORF0tree <- read.tree("ORF0_treefile.txt")

ENV <- ggtree(ENVtree, branch.length = "none", layout = "circular") + geom_tiplab2(size = 4, colour = "blue") + geom_treescale()
POL <- ggtree(POLtree, branch.length = "none", layout = "circular") + geom_tiplab2(size = 4, colour = "blue") + geom_treescale()
GAG <- ggtree(GAGtree, branch.length = "none", layout = "circular") + geom_tiplab2(size = 4, colour = "blue") + geom_treescale()

ORF1 <- ggtree(ORF1tree, branch.length = "none", layout = "circular") + geom_tiplab2(size = 4, colour = "blue") + geom_treescale()
ORF2 <- ggtree(ORF2tree, branch.length = "none", layout = "circular") + geom_tiplab2(size = 4, colour = "blue") + geom_treescale()
ORF0 <- ggtree(ORF0tree, branch.length = "none", layout = "circular") + geom_tiplab2(size = 4, colour = "blue") + geom_treescale()

ENV
POL
GAG
ORF1
ORF2
ORF0

