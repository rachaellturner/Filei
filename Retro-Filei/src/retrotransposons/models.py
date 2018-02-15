from django.db import models

# Create your models here.

# Models correspond to 'tables' in the sqlite3 database.
# Each one is used by other class objects to tell them where they should get their data from
# Changes to these models will not take effect until the 'manage.py makemigrations' and 'manage.py migrate' command are executed.

# model for HERV database
class HERV(models.Model):
    # fields correspond to sqlite3 schema
    swScore = models.IntegerField(blank = True, null = True) # can be empty
    milliDiv = models.IntegerField(blank = True, null = True) # can be empty
    milliDel = models.IntegerField(blank = True, null = True) # can be empty
    milliIns = models.IntegerField(blank = True, null = True) # can be empty
    genoName = models.CharField(max_length = 120) # CharField takes text input
    genoStart = models.IntegerField() # IntegerField takes number input
    genoEnd = models.IntegerField()
    genoLeft = models.IntegerField(blank = True, null = True) # can be empty
    strand = models.CharField(max_length = 1)
    repName = models.CharField(max_length = 120)
    repClass = models.CharField(max_length = 120)
    repFamily = models.CharField(max_length = 120)
    repStart = models.IntegerField(blank = True, null = True) # can be empty
    repEnd = models.IntegerField(blank = True, null= True) # can be empty
    repLeft = models.IntegerField(blank = True, null = True) # can be empty
    DNAseq = models.CharField(max_length = 100000000)
    GAG = models.CharField(max_length = 10000, default = 'None')
    POL = models.CharField(max_length = 10000, default = 'None')
    ENV = models.CharField(max_length = 10000, default = 'None')

    def __str__(self):
        return self.repName # use repname instead of id when calling object identity

# model for LINE1 database
class LINE_1(models.Model):
    # fields correspond to sqlite3 database schema
    swScore = models.IntegerField(blank = True, null=True) # can be empty
    milliDiv = models.IntegerField(blank = True, null = True) # can be empty
    milliDel = models.IntegerField(blank = True, null = True) # can be empty
    milliIns = models.IntegerField(blank = True, null = True) # can be empty
    genoName = models.CharField(max_length = 120) # CharField takes text input
    genoStart = models.IntegerField() # IntegerField takes number input
    genoEnd = models.IntegerField()
    genoLeft = models.IntegerField(blank = True, null=True) # can be empty
    strand = models.CharField(max_length = 1)
    repName = models.CharField(max_length = 120)
    repClass = models.CharField(max_length = 120)
    repFamily = models.CharField(max_length = 120)
    repStart = models.IntegerField(blank = True, null = True) # can be empty
    repEnd = models.IntegerField(blank = True, null = True) # can be empty
    repLeft = models.IntegerField(blank = True, null=True) # can be empty
    DNAseq = models.CharField(max_length = 100000000)
    ORF0 = models.CharField(max_length = 10000, default = 'None')
    ORF1 = models.CharField(max_length = 10000, default = 'None')
    ORF2 = models.CharField(max_length = 10000, default = 'None')

    def __str__(self):
        return self.repName # use repname instead of id when calling object identity

# generic model for uploaded document if needs saving
class Document(models.Model):
    file = models.FileField(upload_to='documents/') # takes a file input
    uploaded_at = models.DateTimeField(auto_now_add=True) # keep track of when document uploaded

class Atlas(models.Model):
    instrument_model = models.CharField(max_length = 1000)
    ionisation_type = models.CharField(max_length = 1000)
    analyser = models.CharField(max_length = 1000)
    detector = models.CharField(max_length = 1000)
    software = models.CharField(max_length = 1000)
    organism = models.CharField(max_length = 1000)
    tissue = models.CharField(max_length = 1000)
    cell_type = models.CharField(max_length = 1000)
    description = models.CharField(max_length = 100000)
    repeat_id = models.CharField(max_length = 1000)
    ORF0 = models.CharField(max_length = 10000,blank = True) # can be empty
    ORF1 = models.CharField(max_length = 10000,blank = True) # can be empty
    ORF2 = models.CharField(max_length = 10000,blank = True) # can be empty
    GAG = models.CharField(max_length = 10000, blank = True) # can be empty
    POL = models.CharField(max_length = 10000,blank = True) # can be empty
    ENV = models.CharField(max_length = 10000,blank = True) # can be empty