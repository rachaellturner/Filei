import django_filters

# get database models from models.py
from .models import HERV, LINE_1, Atlas

# get choice lists from choices.py
from. choices import chromosome_choices, LINE1_choices, HERV_choices


# overwrite lookup_types to have more human readable help text
django_filters.filters.LOOKUP_TYPES = [
#('', '-------------------'),
('exact', 'Is equal to'),
('not_exact', 'Is not equal to'),
('lt', 'Lesser than'),
('gt', 'Greater than'),
('gte', 'Greater than or equal to'),
('lte', 'Lesser than or equal to'),
('startswith', 'Starts with'),
('endswith', 'Ends with'),
('contains', 'Contains'),
('not_contains', 'Does not contain'),
]


# Filter for the HERV model
class simple_HERV_Filter(django_filters.FilterSet):
    
    # variables correspond to fields that will be displayed in the filter on the tables page
    # filter types determine what the user can enter
    # ChoiceFilters use lists from choices.py that the user can select an option from
    
    ID = django_filters.NumberFilter(name = 'id', label = 'ID:') # NumberFilter takes in number input
    Repeat = django_filters.ChoiceFilter(choices = HERV_choices[2:], name = 'repName', label = 'Repeat Name:') # ChoiceFilter uses a drop down menu when rendered
    Class = django_filters.ChoiceFilter(choices = [('LTR','LTR')], name = 'repClass', label = 'Class:')
    Family = django_filters.ChoiceFilter(choices = [('ERVL?','ERVL?'), ('ERVL','ERVL'), ('ERVL-MaLR','ERVL-MaLR'), ('ERV1?','ERV1?'), ('ERV1','ERV1'), ('ERVK','ERVK')], name = 'repFamily', label = 'Family:')
    Chromosome = django_filters.ChoiceFilter(lookup_expr='contains',choices = chromosome_choices, name = 'genoName', label = 'Chromosome:')
    Strand = django_filters.ChoiceFilter(choices = [('+','+'),('-','-')], name = 'strand', label = 'Strand:')    
    Start = django_filters.NumberFilter(name='genoStart', label = 'Start posiiton:')
    End = django_filters.NumberFilter(name='genoEnd', label = 'End position:')
    
    class Meta:
        model = HERV # assign the HERV model to the filter
        fields = [] # fields to be automatically generated would go here, but we have specified all of them explicitly

# Filter model for the LINE_1 model
class simple_LINE1_Filter(django_filters.FilterSet):

    # all options are same as above, but point to the LINE_1 model

    ID = django_filters.NumberFilter(name = 'id', label = 'ID:')
    Repeat = django_filters.ChoiceFilter(choices = LINE1_choices[2:], name = 'repName', label = 'Repeat Name:')
    Class = django_filters.ChoiceFilter(choices = [('LINE','LINE')], name = 'repClass', label = 'Class:')
    Family = django_filters.ChoiceFilter(choices = [('L1','L1')], name = 'repFamily', label = 'Family:')
    Chromosome = django_filters.ChoiceFilter(lookup_expr='contains',choices = chromosome_choices, name = 'genoName', label = 'Chromosome:')
    Strand = django_filters.ChoiceFilter(choices = [('+','+'),('-','-')], name = 'strand', label = 'Strand:')    
    Start = django_filters.NumberFilter(name='genoStart', label = 'Start:')
    End = django_filters.NumberFilter(name='genoEnd', label = 'End:')
    
    class Meta:
        model = LINE_1 # assign the LINE_1 model to the filter
        fields = []

# Filter form for the Atlas model
class Atlas_Filter(django_filters.FilterSet):
    instrument_model = django_filters.CharFilter(label = "Instrument model used:") # CharFilter takes in a text input
    ionisation_type = django_filters.CharFilter(label = "Ionisation type:")
    analyser = django_filters.CharFilter(label = "Analyser:")
    detector = django_filters.CharFilter(label = "Detector:")
    software = django_filters.CharFilter(label = "Software used:")
    organism = django_filters.CharFilter(label = "Organism:")
    tissue = django_filters.CharFilter(label = "Tissue type:")
    cell_type = django_filters.CharFilter(label = "Cell type:")
    description = django_filters.CharFilter(label = "Description (brief):")
    repeat_id = django_filters.CharFilter(label = "Retrotransposon Identified:")
    ORF0 = django_filters.CharFilter(label = "ORF0 sequence:")
    ORF1 = django_filters.CharFilter(label = "ORF1 sequence:")
    ORF2 = django_filters.CharFilter(label = "ORF2 sequence:")
    GAG = django_filters.CharFilter(label = "GAG sequence:")
    POL = django_filters.CharFilter(label = "POL sequence:")
    ENV = django_filters.CharFilter(label = "ENV sequence:")

    class Meta:
        model = Atlas # assign the Atlas model to the filter
        fields = []

