import django_tables2 as tables # import the Table class from the app django_tables2
from django_tables2.export.views import ExportMixin # ExportMixin allows FilterSets to combine with Tables

from .models import HERV, LINE_1, Atlas


# Table for displaying HERV information
class simple_HERV_Table(ExportMixin, tables.Table):
    # Overwrite the default column labels form these fields to make them less obnixious
    repName = tables.Column(verbose_name="Repeat Name")
    repClass = tables.Column(verbose_name="Class")
    repFamily = tables.Column(verbose_name="Family")
    genoName = tables.Column(verbose_name="Chromosome")
    genoStart = tables.Column(verbose_name="Start")
    genoEnd = tables.Column(verbose_name="End")

    class Meta:
        model = HERV
        template = 'django_tables2/bootstrap-responsive.html' # the html template the table will use when it is rendered on the web page
        fields = ("id", "repName", "repClass", "repFamily", "genoName", "genoStart", "genoEnd", "strand") # the fields from the HERV model to include in the table

# Table for displaying LINE_1 information
class simple_LINE1_Table(ExportMixin, tables.Table):
    # Overwrite the default column labels form these fields to make them less obnixious
    repName = tables.Column(verbose_name="Repeat Name")
    repClass = tables.Column(verbose_name="Class")
    repFamily = tables.Column(verbose_name="Family")
    genoName = tables.Column(verbose_name="Chromosome")
    genoStart = tables.Column(verbose_name="Start")
    genoEnd = tables.Column(verbose_name="End")

    class Meta:
        model = LINE_1
        template = 'django_tables2/bootstrap-responsive.html' # the html template the table will use when it is rendered on the web page
        fields = ("id", "repName", "repClass", "repFamily", "genoName", "genoStart", "genoEnd", "strand") # the fields from the LINE_1 model to include in the table

class Atlas_Table(tables.Table):
    class Meta:
        model = Atlas
        template = 'django_tables2/bootstrap-responsive.html'
        # Fields not specified, it'll just use all of them



