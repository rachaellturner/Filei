import pandas
from retrotransposons.models import HERV


def run():

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
    'DNAseq',
    'GAG',
    'POL',
    'ENV'
    ]


    df = pandas.read_csv("HERV_sample.csv.tar.gz", compression = 'gzip', sep = '\t', index_col=None, names = cols)
    
    for row in df.itertuples(): 
        print("Processing " + row.repName)
        HERV.objects.create(
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
            DNAseq = row.DNAseq,
            GAG = row.GAG,
            POL = row.POL,
            ENV = row.ENV
            )
