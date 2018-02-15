from django import forms
from django.core.validators import FileExtensionValidator # calls error messages if files do not have correct extension

# get models from models.py for use in form objects
from .models import Document, LINE_1, HERV, Atlas

# get lists of choices from choices.py for use in form.ChoiceFields()
from .choices import (
    ORF0_choices, 
    ORF1_choices, 
    ORF2_choices, 
    LINE1_choices, 
    GAG_choices, 
    POL_choices, 
    ENV_choices, 
    HERV_choices,
    chromosome_choices
    )

### Document Upload ###

# Form for uploading mzTAB files
class mzTAB_Upload_Form(forms.ModelForm):
    mzTAB = forms.FileField(validators=[FileExtensionValidator(['mztab'])]) # file extension validator tp reject files not ending in .mztab
    class Meta:
        model = Document
        fields = ('mzTAB',)

# Form for uploading mzID files
class mzID_Upload_Form(forms.ModelForm):
    mzID = forms.FileField(validators=[FileExtensionValidator(['mzid'])]) # file extension validator tp reject files not ending in .mzid
    class Meta:
        model = Document
        fields = ('mzID',)

### Protein Logo ### 

# Form for choosing an ORF0 repeat name (select all is excluded)
class ORF0_repname_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ORF0_choices[2:], label = "Repeat name ") # use ORF0 choices, except 'select all'
    class Meta:
        model = LINE_1
        fields = ('repname',)


# Form for choosing an ORF1 repeat name (select all is excluded)
class ORF1_repname_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ORF1_choices[2:], label = "Repeat name ") # use ORF1 choices, except 'select all'
    class Meta:
        model = LINE_1
        fields = ('repname',)

# Form for choosing an ORF2 repeat name (select all is excluded)
class ORF2_repname_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ORF2_choices[2:], label = "Repeat name ") # use ORF2 choices, except 'select all'
    class Meta:
        model = LINE_1
        fields = ('repname',)

# Form for choosing a GAG repeat name (select all is excluded)
class GAG_repname_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = GAG_choices[2:], label = "Repeat name ") # use GAG choices, except 'select all'
    class Meta:
        model = HERV
        fields = ('repname',)

# Form for choosing a POL repeat name (select all is excluded)
class POL_repname_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = POL_choices[2:], label = "Repeat name ") # use POL choices, except 'select all'
    class Meta:
        model = HERV
        fields = ('repname',)

# Form for choosing an ENV repeat name (select all is excluded)
class ENV_repname_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ENV_choices[2:], label = "Repeat name ") # use ENV choices, except 'select all'
    class Meta:
        model = LINE_1
        fields = ('repname',)


### Karyotype ###

# Form for choosing a LINE_1 repeat name (select all is excluded) for the karyotype() function
class LINE1_karyotype_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = LINE1_choices[2:], label="Repeat Name ")
    class Meta:
        model = LINE_1
        fields = ('repname',)

# Form for choosing a HERV repeat name (select all is excluded) for the karyotype() function
class HERV_karyotype_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = HERV_choices[2:], label="Repeat Name ")
    class Meta:
        model = HERV
        fields = ('repname',)


### Find Amino Acid sequence ###

# Form to search the LINE_1 model
class LINE_1_AA_search_Form(forms.ModelForm):
    pep_seq = forms.CharField(required = True, label = "Amino Acid sequence: ") # make required = True so users cant enter a blank string
    class Meta:
        model = LINE_1
        fields = ('pep_seq',)

# Form to search the HERV model
class HERV_AA_search_Form(forms.ModelForm):
    pep_seq = forms.CharField(required = True, label = "Amino Acid sequence: ") # make required = True so users cant enter a blank string
    class Meta:
        model = HERV
        fields = ('pep_seq',)

### DNA Sequences ###

# Form to get DNA sequences from the LINE_1 model by repeat name or ID number
class LINE1_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(required = False, choices = LINE1_choices, label="Repeat Name: ")
    id_num = forms.IntegerField(required = False, label = "ID")

    # attempt at mutually exclusive form fields, however proved buggy (form would not submit)
    '''def clean(self):
        cleaned_data = super(LINE1_sequences_Form, self).clean()  # Get the cleaned data from default clean, returns cleaned_data
        field1 = cleaned_data.get("repname")
        field2 = cleaned_data.get("id_num"),

        if field1 and field2:
            raise forms.ValidationError('Please fill in only Repeat name or ID, not both.')

        return(cleaned_data)'''

    class Meta:
        model = LINE_1
        fields = ('repname','id_num',)

# Form to get DNA sequences from the HERV model by repeat name or ID number
class HERV_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(required = False, choices = HERV_choices, label="Repeat Name ")
    id_num = forms.IntegerField(required = False, label = "ID")

    # attempt at mutually exclusive form fields, however proved buggy (form would not submit)
    '''def clean(self):
        cleaned_data = super(HERV_sequences_Form, self).clean()  # Get the cleaned data from default clean, returns cleaned_data
        field1 = cleaned_data.get("repname")
        field2 = cleaned_data.get("id_num"),

        if field1 and field2:
            raise forms.ValidationError('Please fill in only Repeat name or ID, not both.')

        return(cleaned_data)'''
    
    class Meta:
        model = HERV
        fields = ('repname','id_num',)

## ORF Sequences ###

# Form to choose an ORF0 repeat name from a drop down (select all is included)
class ORF0_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ORF0_choices, label = "Repeat name ")
    class Meta:
        model = LINE_1
        fields = ('repname',)

# Form to choose an ORF2 repeat name from a drop down (select all is included)
class ORF1_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ORF1_choices, label = "Repeat name ")
    class Meta:
        model = LINE_1
        fields = ('repname',)

# Form to choose an ORF2 repeat name from a drop down (select all is included)
class ORF2_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ORF2_choices, label = "Repeat name ")
    class Meta:
        model = LINE_1
        fields = ('repname',)

# Form to choose a GAG repeat name from a drop down (select all is included)
class GAG_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = GAG_choices, label = "Repeat name ")
    class Meta:
        model = HERV
        fields = ('repname',)

# Form to choose a POL repeat name from a drop down (select all is included)
class POL_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = POL_choices, label = "Repeat name ")
    class Meta:
        model = HERV
        fields = ('repname',)

# Form to choose an ENV repeat name from a drop down (select all is included)
class ENV_sequences_Form(forms.ModelForm):
    repname = forms.ChoiceField(choices = ENV_choices, label = "Repeat name ")
    class Meta:
        model = HERV
        fields = ('repname',)


### New Entry ###

# Form for creating a new LINE_1 entry. Form fields correspond to LINE_1 model fields
class LINE1_Entry_Form(forms.ModelForm):
    
    # these fields are marked required = True, they must be filled in to allow submission
    repName = forms.CharField(required = True, label="Name of repeat (required):")
    repClass = forms.CharField(required = True,max_length = 120, label = "Class of repeat (required):")
    repFamily = forms.CharField(required = True,max_length = 120, label = "Family of repeat (required):")
    genoName = forms.ChoiceField(required = True, choices = chromosome_choices, label = "Chromosome (required):")
    genoStart = forms.IntegerField(required = True,label = "Start position in genomic sequence (required):")
    genoEnd = forms.IntegerField(required = True,label = "End position in genomic sequence (required):")
    strand = forms.ChoiceField(required = True,choices = [('+','+'),('-','-')], label = "Relative strand orientation (required):")
    DNAseq = forms.CharField(required = True,max_length = 100000000, label = "DNA sequence (required):")

    # these fields are marked required = False, they do not have to be filled in to submit
    swScore = forms.IntegerField(required = False, label = "Smith Waterman alignment score:")
    milliDiv = forms.IntegerField(required = False, label = "Base mismatches in parts per thousand:")
    milliDel = forms.IntegerField(required = False, label = "Bases deleted in parts per thousand:")
    milliIns = forms.IntegerField(required = False, label = "Bases inserted in parts per thousand:")
    genoLeft = forms.IntegerField(required = False, label = "-#bases after match in genomic sequence:")
    repStart = forms.IntegerField(required = False, label = "Start (if strand is +) or number of bases after match (if strand is -) in repeat sequence:")
    repEnd = forms.IntegerField(required = False, label = "End position in repeat sequence:")
    repLeft = forms.IntegerField(required = False, label = "Number of bases after match (if strand is +) or start (if strand is -) in repeat sequence:")
    ORF0 = forms.CharField(required = False, max_length = 1000000, label = "ORF0 Amino Acid sequence:")
    ORF1 = forms.CharField(required = False, max_length = 1000000, label = "ORF1 Amino Acid sequence:")
    ORF2 = forms.CharField(required = False, max_length = 1000000, label = "ORF2 Amino Acid sequence:")
    
    class Meta:
        model = LINE_1
        fields = ('repName','repClass','repFamily','genoName','genoStart','genoEnd','strand','DNAseq','swScore','milliDiv','milliDel','milliIns','genoLeft','repStart','repEnd','repLeft','ORF0','ORF1','ORF2',)

# Form for creating a new HERV entry. Form fields correspond to HERV model fields
class New_HERV_Entry_Form(forms.ModelForm):
    
    # these fields are marked required = True, they must be filled in to allow submission
    repName = forms.CharField(required = True, label="Name of repeat (required):")
    repClass = forms.CharField(required = True,max_length = 120, label = "Class of repeat (required):")
    repFamily = forms.CharField(required = True,max_length = 120, label = "Family of repeat (required):")
    genoName = forms.ChoiceField(required = True, choices = chromosome_choices, label = "Chromosome (required):")
    genoStart = forms.IntegerField(required = True,label = "Start position in genomic sequence (required):")
    genoEnd = forms.IntegerField(required = True,label = "End position in genomic sequence (required):")
    strand = forms.ChoiceField(required = True,choices = [('+','+'),('-','-')], label = "Relative strand orientation (required):")
    DNAseq = forms.CharField(required = True,max_length = 100000000, label = "DNA sequence (required):")

    # these fields are marked required = False, they do not have to be filled in to submit
    swScore = forms.IntegerField(required = False, label = "Smith Waterman alignment score:")
    milliDiv = forms.IntegerField(required = False, label = "Base mismatches in parts per thousand:")
    milliDel = forms.IntegerField(required = False, label = "Bases deleted in parts per thousand:")
    milliIns = forms.IntegerField(required = False, label = "Bases inserted in parts per thousand:")
    genoLeft = forms.IntegerField(required = False, label = "-#bases after match in genomic sequence:")
    repStart = forms.IntegerField(required = False, label = "Start (if strand is +) or number of bases after match (if strand is -) in repeat sequence:")
    repEnd = forms.IntegerField(required = False, label = "End position in repeat sequence:")
    repLeft = forms.IntegerField(required = False, label = "Number of bases after match (if strand is +) or start (if strand is -) in repeat sequence:")
    GAG = forms.CharField(required = False, max_length = 1000000, label = "ORF0 Amino Acid sequence:")
    POL = forms.CharField(required = False, max_length = 1000000, label = "ORF1 Amino Acid sequence:")
    ENV = forms.CharField(required = False, max_length = 1000000, label = "ORF2 Amino Acid sequence:")

    class Meta:
        model = HERV
        fields = ('repName','repClass','repFamily','genoName','genoStart','genoEnd','strand','DNAseq','swScore','milliDiv','milliDel','milliIns','genoLeft','repStart','repEnd','repLeft','POL','GAG','ENV',)

## Atlas ##

# Form for creating a new Atlas entry. Form fields correspond to Atlas model fields
class Atlas_Form(forms.ModelForm):
    
    # these fields are marked required = True, they must be filled in to allow submission
    instrument_model = forms.CharField(max_length = 1000, required = True, label = "Instrument model used:")
    ionisation_type = forms.CharField(max_length = 1000, required = True, label = "Ionisation type:")
    analyser = forms.CharField(max_length = 1000, required = True, label = "Analyser:")
    detector = forms.CharField(max_length = 1000, required = True, label = "Detector:")
    software = forms.CharField(max_length = 1000, required = True, label = "Software used:")
    organism = forms.CharField(max_length = 1000, required = True, label = "Organism:")
    tissue = forms.CharField(max_length = 1000, required = True, label = "Tissue type:")
    cell_type = forms.CharField(max_length = 1000, required = True, label = "Cell type:")
    description = forms.CharField(max_length = 100000, required = True, label = "Description (brief):")
    repeat_id = forms.CharField(max_length = 1000, required = True, label = "Retrotransposon Identified:")
    
    # these fields are marked required = False, they do not have to be filled in to submit
    ORF0 = forms.CharField(max_length = 10000, required = False, label = "ORF0 sequence identified (if known):")
    ORF1 = forms.CharField(max_length = 10000, required = False, label = "ORF1 sequence identified (if known):")
    ORF2 = forms.CharField(max_length = 10000, required = False, label = "ORF2 sequence identified (if known):")
    GAG = forms.CharField(max_length = 10000, required = False, label = "GAG sequence identified (if known):")
    POL = forms.CharField(max_length = 10000, required = False, label = "POL sequence identified (if known):")
    ENV = forms.CharField(max_length = 10000, required = False, label = "ENV sequence identified (if known):")

    class Meta:
        model = Atlas
        fields = ('instrument_model', 'ionisation_type','analyser','detector','software', 'organism', 'tissue','cell_type','description','repeat_id','ORF0','ORF1','ORF2','GAG','POL','ENV')