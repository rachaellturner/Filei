import pandas
from retrotransposons.models import Retrotransposons

cols  = [
    'swScore', 
    'milliDiv', 
    'milliDel',
    'milliIns',
    'genoName',
    'genoStart',
    'genoEnd', 
    'genoLeft',
    'strand',
    'repName',
    'repClass',
    'repFamily',
    'repStart',
    'repEnd',
    'repLeft',
    'DNAseq'
    ]


df = pandas.read_csv("~/Documents/BIO727P_group_project/first_100_LINES.csv", sep = '\t', index_col=None, skiprows=1, names = cols)

for row in df.itertuples(): 
    print("Processing " + row.repName)
    Retrotransposons.objects.create(
        unique_id = row[0],
        swScore = row.swScore,      
        milliDiv = row.milliDiv, 
        milliDel = row.milliDel, 
        milliIns = row.milliIns, 
        genoName = row.genoName, 
        genoStart = row.genoStart, 
        genoEnd = row.genoEnd, 
        genoLeft = row.genoLeft, 
        strand = row.strand, 
        repName = row.repName, 
        repClass = row.repClass, 
        repFamily = row.repFamily, 
        repStart = row.repStart, 
        repEnd = row.repEnd, 
        repLeft = row.repLeft,
        DNAseq = row.DNAseq
        )
