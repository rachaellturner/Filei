
### conatains lists of choices for use in form ChoiceFields ###

# import the HERV and LINE_1 models
from .models import LINE_1, HERV

''' Live generated choices lists'''

# takes in values list from query set and converts to list of tuples containing each entry twice
# eg ['X','Y'] > [('Select All','Select All'), ('X","X'), ('Y','Y')]
def choice_generator(values_list):
    choices = [('Select All','Select All')]
    for x in values_list:
        choices.append((x[0],x[0]))
    return choices

# choice list of unique ORF0 repeat names
ORF0_choices = choice_generator(sorted(list(set(LINE_1.objects.values_list("repName").exclude(ORF0 = "None")))))
# choice list of unique ORF1 repeat names
ORF1_choices = choice_generator(sorted(list(set(LINE_1.objects.values_list("repName").exclude(ORF1 = "None")))))
# choice list of unique ORF2 repeat names
ORF2_choices = choice_generator(sorted(list(set(LINE_1.objects.values_list("repName").exclude(ORF2 = "None")))))

# choice list of unique GAG repeat names
GAG_choices = choice_generator(sorted(list(set(HERV.objects.values_list("repName").exclude(GAG = "None")))))
# choice list of unique POL repeat names
POL_choices = choice_generator(sorted(list(set(HERV.objects.values_list("repName").exclude(POL = "None")))))
# choice list of unique ENV repeat names
ENV_choices = choice_generator(sorted(list(set(HERV.objects.values_list("repName").exclude(ENV = "None")))))

# choice list of all LINE1 repeat names
LINE1_choices = choice_generator(sorted(list(set(LINE_1.objects.values_list("repName")))))
# choice list of all HERV repeat names
HERV_choices = choice_generator(sorted(list(set(HERV.objects.values_list("repName")))))

# list of tuples containing (repeat name, chromosome) for each entry in LINE1
LINE1_list = list(LINE_1.objects.values_list("repName", "genoName"))
# list of tuples containing (repeat name, chromosome) for each entry in HERV
HERV_list = list(HERV.objects.values_list("repName", "genoName"))

# list of tuples containing (repeat name, chromosome) for each entry with an ORF0 sequence
ORF0_list = list(LINE_1.objects.values_list("repName", "genoName").exclude(ORF0 = "None"))
# list of tuples containing (repeat name, chromosome) for each entry with an ORF1 sequence
ORF1_list = list(LINE_1.objects.values_list("repName", "genoName").exclude(ORF1 = "None"))
# list of tuples containing (repeat name, chromosome) for each entry with an ORF2 sequence
ORF2_list = list(LINE_1.objects.values_list("repName", "genoName").exclude(ORF2 = "None"))

# list of tuples containing (repeat name, chromosome) for each entry with a GAG sequence
GAG_list = list(HERV.objects.values_list("repName", "genoName").exclude(GAG = "None"))
# list of tuples containing (repeat name, chromosome) for each entry with a POL sequence
POL_list = list(HERV.objects.values_list("repName", "genoName").exclude(POL = "None"))
# list of tuples containing (repeat name, chromosome) for each entry with an ENV sequence
ENV_list = list(HERV.objects.values_list("repName", "genoName").exclude(ENV = "None"))

'''Pre-generated choices lists'''

# choice list of all chromosomes used in various functions
chromosome_choices = [('chr1', 'chr1'), ('chr2', 'chr2'), ('chr3', 'chr3'), ('chr4', 'chr4'), ('chr5', 'chr5'), ('chr6', 'chr6'), ('chr7', 'chr7'), ('chr8', 'chr8'), ('chr9', 'chr9'), ('chr10', 'chr10'), ('chr11', 'chr11'), ('chr12', 'chr12'), ('chr13', 'chr13'), ('chr14', 'chr14'), ('chr15', 'chr15'), ('chr16', 'chr16'), ('chr17', 'chr17'), ('chr18', 'chr18'), ('chr19', 'chr19'), ('chr20', 'chr20'), ('chr21', 'chr21'), ('chr22', 'chr22'), ('chrX', 'chrX'), ('chrY', 'chrY')]


