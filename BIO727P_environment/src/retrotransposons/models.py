from django.db import models

# Create your models here.

class Retrotransposons(models.Model):
    unique_id = models.IntegerField(unique = True)
    swScore = models.IntegerField()
    milliDiv = models.IntegerField()
    milliDel = models.IntegerField()
    milliIns = models.IntegerField()
    genoName = models.CharField(max_length = 120)
    genoStart = models.IntegerField()
    genoEnd = models.IntegerField()
    genoLeft = models.IntegerField()
    strand = models.CharField(max_length = 1)
    repName = models.CharField(max_length = 120, )
    repClass = models.CharField(max_length = 120)
    repFamily = models.CharField(max_length = 120)
    repStart = models.IntegerField()
    repEnd = models.IntegerField()
    repLeft = models.IntegerField()

    def __str__(self):
        return self.repName
