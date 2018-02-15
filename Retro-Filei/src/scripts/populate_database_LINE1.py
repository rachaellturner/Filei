import pandas
from retrotransposons.models import LINE_1


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
    'ORF0',
    'ORF1',
    'ORF2'
    ]
    
    df = pandas.read_csv("LINE1_sample.csv.tar.gz",compression='gzip', sep = '\t', index_col=None, skiprows=1, names = cols)
    
    for row in df.itertuples():
        print("Processing " + row.repName)
            
        LINE_1.objects.create(
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
            ORF0 = row.ORF0,
            ORF1 = row.ORF1,
            ORF2 = row.ORF2
            )

