# delete ''' from start and end of file when instructed!
'''

from django.shortcuts import render, render_to_response
from django.views import View
from django.db.models import Q # extended filter options

from django_tables2 import RequestConfig # configure tables using csrf token
from django_tables2.export.export import TableExport # for exporting csv
from django_tables2.views import SingleTableMixin # for mixing django_tables2 and django_filters

# get database models from models.py
from .models import ( 
    HERV, 
    LINE_1,
    Atlas
    )

# get table objects from tables.py
from .tables import (
    simple_LINE1_Table, 
    simple_HERV_Table,
    Atlas_Table
    )

# get filter objects from filters.py
from .filters import (
    simple_LINE1_Filter, 
    simple_HERV_Filter, 
    Atlas_Filter
    )

# get choice lists from choices.py
from .choices import (
    ORF0_list, 
    ORF1_list, 
    ORF2_list, 
    GAG_list, 
    POL_list, 
    ENV_list,
    LINE1_list,
    HERV_list
    )

# get forms from forms.py
from .forms import (
    ORF0_repname_Form, 
    ORF1_repname_Form, 
    ORF2_repname_Form, 
    LINE1_karyotype_Form, 
    GAG_repname_Form, 
    POL_repname_Form, 
    ENV_repname_Form, 
    HERV_karyotype_Form, 
    LINE1_sequences_Form,
    HERV_sequences_Form,
    ORF0_sequences_Form,
    ORF1_sequences_Form,
    ORF2_sequences_Form,
    GAG_sequences_Form,
    POL_sequences_Form,
    ENV_sequences_Form,
    mzID_Upload_Form,
    mzTAB_Upload_Form,
    LINE1_Entry_Form,
    New_HERV_Entry_Form,
    Atlas_Form,
    LINE_1_AA_search_Form,
    HERV_AA_search_Form
    )

### python modules ###

import pandas
import numpy as np
import matplotlib
matplotlib.use('Agg') # avoid backend problems due to no X11 or TKinter by using AGG
import matplotlib.pyplot as plt

from collections import Counter, OrderedDict # used in karytype function
from textwrap import TextWrapper # used in protein logo function

### rpy2 ###

import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects.lib import ggplot2
from rpy2.robjects import r, pandas2ri

# activate pandas2ri to make its functions work
pandas2ri.activate()

# R packages to import
ggbio = importr('ggbio')
GenomicRanges = importr('GenomicRanges')
IRanges = importr('IRanges')
karyoploteR = importr('karyoploteR')
mzID = importr('mzID')
Biostrings = importr('Biostrings')
msa = importr('msa')
ggseqlogo = importr('ggseqlogo')

### r base ### 
nrow = ro.r['nrow']
dataframe = ro.r['data.frame']
length = ro.r['length']
tostring = ro.r['toString']


# Create your views here.


### Tables ###

# Table for HERV database
def simple_HERV_table(request):
    template_name = 'retrotransposons/table.html'
    family = 'HERV'
    
    f = simple_HERV_Filter(request.GET, queryset=HERV.objects.all())

    table = simple_HERV_Table(f.qs)
    
    RequestConfig(request).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))
    
    context = {'table':table, 'filter': f, 'family':family}
    
    return render(request, template_name, context)
# Table for LINE_1 database
def simple_LINE1_table(request):
    template_name = 'retrotransposons/table.html'
    family = 'LINE1'
    
    f = simple_LINE1_Filter(request.GET, queryset=LINE_1.objects.all())

    table = simple_LINE1_Table(f.qs)
    
    RequestConfig(request).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))
    
    context = {'table':table, 'filter': f, 'family': family}
    
    return render(request, template_name, context)
# Table for Atlas database
def Atlas_table(request):
    family = 'Atlas'
    f = Atlas_Filter(request.GET, queryset=Atlas.objects.all())

    table = Atlas_Table(f.qs)
    
    RequestConfig(request).configure(table)
    
    context = {'table':table, 'filter': f, 'family': family}
    
    return render(request,"retrotransposons/table.html", {'family':family,'filter':f,'table':table})

### chart graphics ###

# chromosome stacked bar plot
def stacked_plot_chr(family):
    chromosome_list=["chr1","chr2","chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chrX", "chrY"]
    
    if family == 'LINE1':

        repNamelist_orf0 = []
        chrlist_orf0 = []

        for i in ORF0_list: # see choices.py, format is (repeat name,chromosome)
            if i[1] in chromosome_list: # check if chromosome is in chromo_some list (reject weird names)
                repNamelist_orf0.append(i[0]) # add repeat name from tuple
                chrlist_orf0.append(i[1]) # add chromosome from tuple

        t=Counter(chrlist_orf0) # count the number of each chromosome
        g1=OrderedDict(t) # sort chromosomes into order
        for entry in chromosome_list:
            try:
                g1.move_to_end(entry)
            except:
                continue

        # same again for ORF1
        repNamelist_orf1=[]
        chrlist_orf1=[]

        for i in ORF1_list:
            if i[1] in chromosome_list:
                repNamelist_orf1.append(i[0])
                chrlist_orf1.append(i[1])

        h=Counter(chrlist_orf1)
        h1=OrderedDict(h)
        for entry in chromosome_list:
            try:
                h1.move_to_end(entry)
            except:
                continue

        repNamelist_orf2=[]
        chrlist_orf2=[]

        # same again for ORF2
        for i in ORF2_list:
            if i[1] in chromosome_list:
                repNamelist_orf2.append(i[0])
                chrlist_orf2.append(i[1])

        v=Counter(chrlist_orf2)
        v1=OrderedDict(v)
        for entry in chromosome_list:
            try:
                v1.move_to_end(entry)
            except:
                continue

    elif family == 'HERV':
        # same as above, using HERV opening reading frames
        repNamelist_gag = []
        chrlist_gag = []

        for i in GAG_list:
            if i[1] in chromosome_list:
                repNamelist_gag.append(i[0])
                chrlist_gag.append(i[1])

        t=Counter(chrlist_gag)
        g1=OrderedDict(t)
        for entry in chromosome_list:
            try:
                g1.move_to_end(entry)
            except:
                continue

        repNamelist_pol=[]
        chrlist_pol=[]

        for i in POL_list:
            if i[1] in chromosome_list:
                repNamelist_pol.append(i[0])
                chrlist_pol.append(i[1])

        h=Counter(chrlist_pol)
        h1=OrderedDict(h)
        for entry in chromosome_list:
            try:
                h1.move_to_end(entry)
            except:
                continue

        repNamelist_env=[]
        chrlist_env=[]

        for i in ENV_list:
            if i[1] in chromosome_list:
                repNamelist_env.append(i[0])
                chrlist_env.append(i[1])

        v=Counter(chrlist_env)
        v1=OrderedDict(v)
        for entry in chromosome_list:
            try:
                v1.move_to_end(entry)
            except:
                continue

    all_dicts=[g1, h1, v1] # combine dictionaries into  list

    super_dict_keys=[]           

    for d in all_dicts:
        for x in d:
            if x not in super_dict_keys:
                super_dict_keys.append(x)

    # create super dictionary
    super_dict=OrderedDict((x,[0]) for x in super_dict_keys)  # "empty dictionary"

    # for each key in the dictionary add the values from g1, h1, v1 in that order, including zero values
    for x in super_dict:
        for y in all_dicts:
            if x in y:
                (super_dict[x]).append(y[x])
            else:
                (super_dict[x]).append(0)
    
    # sort chromosomes into order for x-axis on graph
    for entry in chromosome_list:
        try:
            super_dict.move_to_end(entry)
        except:
                continue

    #PLOTTING STACKED BAR PLOT
    N=len(super_dict)

    #create empty lists
    c=[]
    v=[]
    #key and values in super_dict dictionary is sperated into two lists
    for key, val in super_dict.items():
        c.append(key)
        v.append(val)

    v=np.array(v)

    #plot stack bar plot
    p1=plt.bar(range(len(c)), v[:,1])
    p2=plt.bar(range(len(c)), v[:,2], bottom =v[:,1])
    p3=plt.bar(range(len(c)), v[:,3], bottom=v[:,1]+v[:,2]) 
    plt.xticks(range(len(c)), c, rotation=90)
    if family == 'LINE1':
        plt.legend((p1[0],p2[0],p3[0]), ('ORF0', 'ORF1', 'ORF2')) # names for the LINE_1 legend
    elif family == 'HERV':
        plt.legend((p1[0],p2[0],p3[0]), ('GAG', 'POL', 'ENV')) # names for the HERV legend
    plt.savefig("retrotransposons/static/images/stacked_plot_chr.png") # save the file as a png in the static folder
    
    print("Made Graph") # indicate in terminal that the code has worked
    
    # command that make python forget the previous plot or it'll behave wierdly on page refresh
    plt.clf()
    plt.cla()
    plt.close()

# repname stacked bar plot
def stacked_plot_repname(family):
    chromosome_list=["chr1","chr2","chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chrX", "chrY"]
    
    # code mostly same as stacked_plot_chr, but plots repeat names
    # differences are commented

    if family == 'LINE1':

        repNamelist_orf0 = []
        chrlist_orf0 = []

        for i in ORF0_list:
            if i[1] in chromosome_list:
                repNamelist_orf0.append(i[0])
                chrlist_orf0.append(i[1])

        t=Counter(repNamelist_orf0) # counter uses repeat names list instead 
        g1=OrderedDict(t)
        for entry in chromosome_list:
            try:
                g1.move_to_end(entry)
            except:
                continue

        repNamelist_orf1=[]
        chrlist_orf1=[]

        for i in ORF1_list:
            if i[1] in chromosome_list:
                repNamelist_orf1.append(i[0])
                chrlist_orf1.append(i[1])

        h=Counter(repNamelist_orf1)
        h1=OrderedDict(h)
        for entry in chromosome_list:
            try:
                h1.move_to_end(entry)
            except:
                continue

        repNamelist_orf2=[]
        chrlist_orf2=[]

        for i in ORF2_list:
            if i[1] in chromosome_list:
                repNamelist_orf2.append(i[0])
                chrlist_orf2.append(i[1])

        v=Counter(repNamelist_orf2)
        v1=OrderedDict(v)
        for entry in chromosome_list:
            try:
                v1.move_to_end(entry)
            except:
                continue

    elif family == 'HERV':

        repNamelist_gag = []
        chrlist_gag = []

        for i in GAG_list:
            if i[1] in chromosome_list:
                repNamelist_gag.append(i[0])
                chrlist_gag.append(i[1])

        t=Counter(repNamelist_gag)
        g1=OrderedDict(t)
        for entry in chromosome_list:
            try:
                g1.move_to_end(entry)
            except:
                continue

        repNamelist_pol=[]
        chrlist_pol=[]

        for i in POL_list:
            if i[1] in chromosome_list:
                repNamelist_pol.append(i[0])
                chrlist_pol.append(i[1])

        h=Counter(repNamelist_pol)
        h1=OrderedDict(h)
        for entry in chromosome_list:
            try:
                h1.move_to_end(entry)
            except:
                continue

        repNamelist_env=[]
        chrlist_env=[]

        for i in ENV_list:
            if i[1] in chromosome_list:
                repNamelist_env.append(i[0])
                chrlist_env.append(i[1])

        v=Counter(repNamelist_env)
        v1=OrderedDict(v)
        for entry in chromosome_list:
            try:
                v1.move_to_end(entry)
            except:
                continue

    all_dicts=[g1, h1, v1]

    super_dict_keys=[]           

    for d in all_dicts:
        for x in d:
            if x not in super_dict_keys:
                super_dict_keys.append(x)
    
    # sort chromosomes into order for x-axis on graph
    for entry in chromosome_list:
        try:
            super_dict.move_to_end(entry)
        except:
                continue

    # create super dictionary
    super_dict=OrderedDict((x,[0]) for x in super_dict_keys)  # "empty dictionary"

    # for each key in the dictionary add the values from g1, h1, v1 in that order, including zero values
    for x in super_dict:
        for y in all_dicts:
            if x in y:
                (super_dict[x]).append(y[x])
            else:
                (super_dict[x]).append(0)

    #PLOTTING STACKED BAR PLOT
    N=len(super_dict)

    #create empty lists
    c=[]
    v=[]
    #key and values in super_dict dictionary is sperated into two lists
    for key, val in super_dict.items():
        c.append(key)
        v.append(val)

    v=np.array(v)

    #plot stack bar plot
    p1=plt.bar(range(len(c)), v[:,1])
    p2=plt.bar(range(len(c)), v[:,2], bottom =v[:,1])
    p3=plt.bar(range(len(c)), v[:,3], bottom=v[:,1]+v[:,2]) 
    plt.xticks(range(len(c)), c, rotation=90)
    # add tight layout to fit x axis labels in
    plt.tight_layout(pad = 1.3)
    if family == 'LINE1':
        plt.legend((p1[0],p2[0],p3[0]), ('ORF0', 'ORF1', 'ORF2'))
    elif family == 'HERV':
        plt.legend((p1[0],p2[0],p3[0]), ('GAG', 'POL', 'ENV'))
    plt.savefig("retrotransposons/static/images/stacked_plot_repname.png")

    # forget the previous plot or it'll behave wierdly on page refresh
    plt.clf()
    plt.cla()
    plt.close()

# chromosome bat chart

def bar_plot_chr(family):
    chromosome_list=["chr1","chr2","chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chrX", "chrY"]
    
    if family == 'LINE1':

        repNamelist = []
        chrlist = []

        for i in LINE1_list:
            if i[1] in chromosome_list:
                repNamelist.append(i[0])
                chrlist.append(i[1])

    elif family == 'HERV':

        repNamelist = []
        chrlist = []

        for i in HERV_list:
            if i[1] in chromosome_list:
                repNamelist.append(i[0])
                chrlist.append(i[1])

    t=Counter(chrlist)
    d=OrderedDict(t)
    for entry in chromosome_list:
        try:
            d.move_to_end(entry)
        except:
            continue

    #Values= the number of repeats, keys= chromosome\
    nChr=d.values()
    Chr =d.keys() 
    #range of the x axis
    ChrAsX= range(len(d))
    #plot(x,y)
    plt.bar(ChrAsX, nChr)
    #adjusting plot visualisations\
    plt.xticks(ChrAsX, Chr, rotation=20) # x axis labels
    plt.xlim([min(ChrAsX)- 0.3, max(ChrAsX)+1]) # set x axis limit 
    plt.ylim([0,max(nChr)+5000]) # set y axis limit
    plt.grid(True, axis='y') 
    plt.rc('xtick', labelsize=8) # set label size
    plt.rc('ytick', labelsize=8) # set label size
    plt.title('Frequency of ' + family + ' repeats in each chromosome ') # add a title
    plt.xlabel('Chromosomes') # add x axis name
    plt.ylabel('Frequency') # add y axis name

    #view plot
    fig= plt.gcf()
    fig.set_size_inches(10,10)
    plt.savefig("retrotransposons/static/images/bar_plot_chr.png") # save the plot to a png file, in the static folder

    plt.clf()
    plt.cla()
    plt.close()

def bar_plot_repname(family):
    chromosome_list=["chr1","chr2","chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chrX", "chrY"]
    
    # as bar_plot_chr, but counts repeat names instead

    if family == 'LINE1':

        repNamelist = []
        chrlist = []

        for i in LINE1_list:
            if i[1] in chromosome_list:
                repNamelist.append(i[0])
                chrlist.append(i[1])

    elif family == 'HERV':

        repNamelist = []
        chrlist = []

        for i in HERV_list:
            if i[1] in chromosome_list:
                repNamelist.append(i[0])
                chrlist.append(i[1])

    t=Counter(repNamelist) # count the number of each repeat name
    d=OrderedDict(t)
    for entry in chromosome_list:
        try:
            d.move_to_end(entry)
        except:
            continue

    #Values= the number of repeats, keys= chromosome\
    nChr=d.values()
    Chr =d.keys() 
    
    #range of the x axis
    ChrAsX= range(len(d))

    plt.bar(ChrAsX, nChr)

    plt.xticks(ChrAsX, Chr, rotation=90)
    plt.xlim([min(ChrAsX)- 0.3, max(ChrAsX)+1])
    plt.ylim([0,max(nChr)+5000])
    plt.grid(True, axis='y')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)

    plt.title('Frequency of repeats accross the Human genome')
    plt.xlabel('Repeat names')
    plt.ylabel('Frequency')

    fig= plt.gcf()
    fig.set_size_inches(20,10)

    plt.savefig("retrotransposons/static/images/bar_plot_repname.png")

    plt.clf()
    plt.cla()
    plt.close()


### mzTAB ###

# upload mztab, compare to LINE_1 database
def LINE1_upload_mztab_file(request):
    family = 'LINE1'
    if request.method == 'POST':
        form = mzTAB_Upload_Form(request.POST, request.FILES) # gets post request from upload form
        if form.is_valid():
            
            results = mztab_parser(request.FILES['mzTAB']) # invoke the mzTAB_parser function on the uploaded file
            
            matches = 0 # count matches
            query_sets = [] # list of non-empty query sets
            hits = [] # list of peptide sequences that correspond with non-empty query sets
            for pep_seq in results:
                print(pep_seq)
                # generate a query set for each repeat using the LINE_1 model, looking for orf sequences that contain the peptide sequence
                info = LINE_1.objects.filter(Q(ORF0__icontains=pep_seq) | Q(ORF1__icontains=pep_seq) | Q(ORF2__icontains=pep_seq))
                if info.exists(): # if the queryset isn't empty
                    query_sets.append(info)
                    matches += 1
                    hits.append(pep_seq)

            output = zip(hits, query_sets) # combine lists to iterate over both query sets and hits in the html

            context = {'output':output, 'family':family, 'matches':matches, 'hits':hits}
         
            return render(request, 'retrotransposons/mz_results.html', context)
          
    else:
        form = mzTAB_Upload_Form()
    return render(request, 'retrotransposons/upload_mzTab_file.html', {'form': form, 'family': family})

# upload mztab, compare to HERV database
def HERV_upload_mztab_file(request):
    family = 'HERV'
    if request.method == 'POST':
        form = mzTAB_Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            
            results = mztab_parser(request.FILES['mzTAB'])

            matches = 0 # count matches
            query_sets = [] # list of non-empty query sets
            hits = [] # list of peptide sequences that correspond with non-empty query sets
            for pep_seq in results:
                print(pep_seq) # show in terminal that this is actually doing something!
                # generate a query set for each repeat using the HERV model, looking for orf sequences that contain the peptide sequence
                info = HERV.objects.filter(Q(GAG__icontains=pep_seq) | Q(POL__icontains=pep_seq) | Q(ENV__icontains=pep_seq))
                if info.exists():
                    query_sets.append(info)
                    matches += 1
                    hits.append(pep_seq)

            output = zip(hits, query_sets) # combine lists to iterate over both query sets and hits in the html

            context = {'output':output, 'family':family, 'matches':matches, 'hits':hits}
            
            return render(request, 'retrotransposons/mz_results.html', context)
          
    else:
        form = mzTAB_Upload_Form()
    return render(request, 'retrotransposons/upload_mzTab_file.html', {'form': form, 'family': family})

# function for extracting info from mztab file
def mztab_parser(mzTabfile):
    PSMsequences = [] #list containing sequences from PSM. 

    for line in mzTabfile.readlines():
        
        splitline = line.decode().split() #split lines by whitespace. ##Owen: added .decode() method to make this work

        if "PSM" in splitline: #lines starting with PSM contain sequences.
            PSMsequences.append(splitline[1]) #takes out sequence.

    if PSMsequences == []:
        print("No PSM sequences found.")
    elif PSMsequences != []:
        print(set(PSMsequences))
    
    results = list(set(PSMsequences)) # use set to get remove repeat pep_seqs

    return results

### mzID ###

# upload mzID, compare to LINE_1 database
def LINE1_upload_mzID_file(request):
    family = 'LINE1'
    filepath = 'retrotransposons/static/upload.mzid'

    if request.method == 'POST':
        form = mzID_Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            
            upload_file = request.FILES['mzID']

            # need to write a local copy of the uploaded file. mzID R package will not work on temporary files
            with open('retrotransposons/static/upload.mzid', 'wb+') as destination:
                for chunk in upload_file.chunks(): # chunk avoids memory issues on large files
                    destination.write(chunk)
            
            results = mzID_parser(filepath) # invoke the mzID_parser function on the copied file
            
            matches = 0 # count matches
            hits = [] # list of peptide sequences that result non-empty query sets
            query_sets = [] # list of non-empty query sets
            for pep_seq in results:
                print(pep_seq)
                # generate a query set for each repeat using the LINE_1 model, looking for orf sequences that contain the peptide sequence
                info = LINE_1.objects.filter(Q(ORF0__icontains=pep_seq) | Q(ORF1__icontains=pep_seq) | Q(ORF2__icontains=pep_seq))
                if info.exists():
                    query_sets.append(info)
                    matches += 1
                    hits.append(pep_seq)
            
            output = zip(hits, query_sets) # combine lists to iterate over both query sets and hits in the html

            context = {'output':output, 'family':family, 'matches':matches, 'hits':hits}

            return render(request, 'retrotransposons/mz_results.html', context)
    else:
        form = mzID_Upload_Form()
    return render(request, 'retrotransposons/upload_mzID_file.html', {'form': form, 'family': family})

# upload mzID, compare to HERV database
def HERV_upload_mzID_file(request):
     # as LINE1_upload_mzID_file(), but uses the HERV model to generate a queryset

    family = 'HERV'
    filepath = 'retrotransposons/static/upload.mzid'

    if request.method == 'POST':
        form = mzID_Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            
            # need to write a local copy of the uploaded file. mzID R package will not work on temporary files
            upload_file = request.FILES['mzID']
            with open('retrotransposons/static/upload.mzid', 'wb+') as destination:
                for chunk in upload_file.chunks():  # chunk avoids memory issues on large files
                    destination.write(chunk)
            
            results = mzID_parser(filepath) # invoke the mzID_parser function on the copied file
            
            matches = 0 # count number of matches
            hits = [] # list of peptide sequences that correspond to non-empty query sets
            query_sets = [] # list of non-empty query sets
            for pep_seq in results:
                print(pep_seq)
                # generate a query set for each repeat using the HERV model, looking for orf sequences that contain the peptide sequence
                info = HERV.objects.filter(Q(GAG__icontains=pep_seq) | Q(POL__icontains=pep_seq) | Q(ENV__icontains=pep_seq))
                if info.exists():
                    query_sets.append(info)
                    matches += 1
                    hits.append(pep_seq)

            output = zip(hits, query_sets) # combine lists to iterate over both query sets and hits in the html

            context = {'output':output, 'family':family, 'matches':matches, 'hits':hits}
            
            return render(request, 'retrotransposons/mz_results.html', context)
    else:
        form = mzID_Upload_Form()
    return render(request, 'retrotransposons/upload_mzID_file.html', {'form': form, 'family': family})

# function for extracting info from mzID file
def mzID_parser(filepath):
    mzresults = mzID.mzID(filepath) # get the information from the mzID file

    flatten_results = mzID.flatten(mzresults) # turn it into an accessible format

    df = pandas2ri.ri2py(flatten_results) # convert R format to pandas dataframe

    no_decoys = df[df['isdecoy']==0] #0 is logical FALSE, remove decoy sequences from the dataframe

    # add all peptide sequences found to a list
    pep_seqs = []
    for (idx,row) in no_decoys.iterrows():
        pep_seqs.append(row.loc['pepseq'])

    unique_pep_seqs = list(set(pep_seqs)) # remove duplicate peptide sequences

    return(unique_pep_seqs)

### Protein Logo ###
# functon for generating protein logo image
def protein_logo(filepath):
    MySequences = Biostrings.readAAStringSet(filepath) # read in fasta file generated from queryset
    num_seqs = (length(MySequences)[0]) # count the number of sequences in the file

    if num_seqs == 1: # exception for single sequences (no need to run alignment on a single sequence!)

        seq = str((tostring(MySequences))[0])

        wrapper = TextWrapper(break_on_hyphens=False,width = 40)
        fragments = wrapper.wrap(seq)
        rows = len(fragments)

        with open("retrotransposons/static/alignment.txt", "w") as output:
            output.write(seq)

        height = len(fragments)*250

        # code for removing axis text, was unable to get this working inside django. Works fine as its own script!
        #gp = ggseqlogo.ggseqlogo(fragments, nrow = rows)
        #pp = ggplot2.theme(
            #axis_text = ggplot2.element_blank(),
            #strip_text_x = ggplot2.element_blank(),
            #axis_title_y = ggplot2.element_blank(),
            #axis_text_y = ggplot2.element_blank())
    
        ro.r.jpeg(file = 'retrotransposons/static/images/protein_logo_image.jpg', width = 1150, height = height, units = "px")
        print(ggseqlogo.ggseqlogo(fragments, nrow = rows))
        ro.r('dev.off()')
    
        return()
    
    # align the sequences using msa
    Alignment = msa.msa(MySequences)

    Alignment2 = msa.msaConvert(Alignment, type="seqinr::alignment")

    #pull out he sequences from the alignment
    sequences = Alignment2.rx('seq')

    # pull out the consensus sequence produced from the alignment
    consensus = msa.msaConsensusSequence(Alignment)[0]

    # number of sequences
    nrows = nrow(dataframe(sequences))[0]

    # make a list of the sequences in the alignment
    seqs = []
    for n in range(0,nrows):
        seqs.append(sequences[0][n])

    # write the sequence alignment out to a text document that the user can download
    with open("retrotransposons/static/alignment.txt", "w") as output:
        for x in seqs:
            output.write(x+"\n")
        output.write("\n"+"Consensus sequence:"+"\n"+consensus)

    # need to split the aligned sequences into shorter sequences using TextWrapper
    fragments =[] 
    for x in seqs: 
        wrapper = TextWrapper(break_on_hyphens=False,width = 40)
        y = wrapper.wrap(x)
        fragments.append(y)

    # put the sequence fragments together with their corresponding fragments from the same positions
    zipped_fragments = list(map(list,zip(*fragments)))

    height = len(zipped_fragments)*250 # set the height of the image generated relative to the number of sequence fragments

    rows = len(zipped_fragments) 

    #gp = ggseqlogo.ggseqlogo(zipped_fragments, nrow = rows)
    #pp = ggplot2.theme(
        #axis_text = ggplot2.element_blank(),
        #strip_text_x = ggplot2.element_blank(),
        #axis_title_y = ggplot2.element_blank(),
        #axis_text_y = ggplot2.element_blank()
        #)

    ro.r.jpeg(file = 'retrotransposons/static/images/protein_logo_image.jpg', width = 1200, height = height, units = "px")    
    print(ggseqlogo.ggseqlogo(zipped_fragments, nrow = rows)) # ggseqlogo produces the alignment image 
    ro.r('dev.off()')

# functions for processing info from database for each orf in LINE_1 and HERV into protein logos   
def ORF0_protein_logo(request):
    family = 'LINE1'
    orf = 'ORF0'
    template_name = "retrotransposons/alignment.html"
    if request.method == 'POST':
        form = ORF0_repname_Form(request.POST)
        if form.is_valid():
            repname = form.cleaned_data['repname'] # get the repeat name to use from the user

            # generate a filter set containing required information to produce a fasta file 
            info = list(LINE_1.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "strand", "ORF0").exclude(ORF0 = 'None'))
            filepath = "retrotransposons/static/protein_logo.fasta"

            # generate fasta file from the query set (BioStrings will only take this input to produce a format msa will understand)
            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry[0])+";"+str(entry[1])+"-"+str(entry[2])+";"+str(entry[3])+"\n"+str(entry[4])+"\n")
            
            protein_logo(filepath)
            image = True # tell the webpage to include the image now that it has been generated
            return render(request, template_name, {'form':form, 'image':image, 'family':family, 'orf':orf, 'repname':repname})
        
    else:
        form = ORF0_repname_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

def ORF1_protein_logo(request):
    # same as ORF0_protein_logo, but uses an ORF1 queryset

    family = 'LINE1'
    orf = 'ORF1'
    template_name = "retrotransposons/alignment.html"
    if request.method == 'POST':
        form = ORF1_repname_Form(request.POST)
        if form.is_valid():
            repname = form.cleaned_data['repname']
            info = list(LINE_1.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "strand", "ORF1").exclude(ORF1 = 'None'))
            filepath = "retrotransposons/static/protein_logo.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry[0])+";"+str(entry[1])+"-"+str(entry[2])+";"+str(entry[3])+"\n"+str(entry[4])+"\n")
            
            protein_logo(filepath)
            image = True
            return render(request, template_name, {'form':form, 'image':image, 'family':family, 'orf': orf, 'repname':repname})
        
    else:
        form = ORF1_repname_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

def ORF2_protein_logo(request):
    # same as ORF0_protein_logo, but uses an ORF2 queryset

    family = 'LINE1'
    orf = 'ORF2'
    template_name = "retrotransposons/alignment.html"
    if request.method == 'POST':
        form = ORF2_repname_Form(request.POST)
        if form.is_valid():
            repname = form.cleaned_data['repname']
            info = list(LINE_1.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "strand", "ORF2").exclude(ORF2 = 'None'))
            filepath = "retrotransposons/static/protein_logo.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry[0])+";"+str(entry[1])+"-"+str(entry[2])+";"+str(entry[3])+"\n"+str(entry[4])+"\n")
            
            protein_logo(filepath)
            image = True
            return render(request, template_name, {'form':form, 'image':image, 'family':family, 'orf':orf, 'repname':repname})
        
    else:
        form = ORF2_repname_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})       

def GAG_protein_logo(request):
    # same as ORF0_protein_logo, but uses a GAG queryset from the HERV model

    family = 'HERV'
    orf = 'GAG'
    template_name = "retrotransposons/alignment.html"
    if request.method == 'POST':
        form = GAG_repname_Form(request.POST)
        if form.is_valid():
            repname = form.cleaned_data['repname']
            
            info = list(HERV.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "strand", "GAG").exclude(GAG = 'None'))
            
            filepath = "retrotransposons/static/protein_logo.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry[0])+";"+str(entry[1])+"-"+str(entry[2])+";"+str(entry[3])+"\n"+str(entry[4])+"\n")
            
            protein_logo(filepath)
            
            image = True
            
            return render(request, template_name, {'form':form, 'image':image, 'family':family, 'orf':orf, 'repname':repname})
        
    else:
        form = GAG_repname_Form()
    return render(request, template_name, {'form':form, 'family':family, 'orf':orf})

def POL_protein_logo(request):
    # same as ORF0_protein_logo, but uses a POL queryset from the HERV model

    family = 'HERV'
    orf = 'POL'
    template_name = "retrotransposons/alignment.html"
    if request.method == 'POST':
        form = POL_repname_Form(request.POST)
        if form.is_valid():
            repname = form.cleaned_data['repname']
            info = list(HERV.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "strand", "POL").exclude(POL = 'None'))
            filepath = "retrotransposons/static/protein_logo.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry[0])+";"+str(entry[1])+"-"+str(entry[2])+";"+str(entry[3])+"\n"+str(entry[4])+"\n")
            
            protein_logo(filepath)
            image = True
            return render(request, template_name, {'form':form, 'image':image, 'family':family, 'orf':orf, 'repname':repname})
        
    else:
        form = POL_repname_Form()
    return render(request, template_name, {'form':form, 'family':family, 'orf':orf})

def ENV_protein_logo(request):
    # same as ORF0_protein_logo, but uses an ENV queryset from the HERV model

    family = 'HERV'
    orf = 'ENV'
    template_name = "retrotransposons/alignment.html"
    if request.method == 'POST':
        form = ENV_repname_Form(request.POST)
        if form.is_valid():
            repname = form.cleaned_data['repname']
            info = list(HERV.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "strand", "ENV").exclude(ENV = 'None'))
            filepath = "retrotransposons/static/protein_logo.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry[0])+";"+str(entry[1])+"-"+str(entry[2])+";"+str(entry[3])+"\n"+str(entry[4])+"\n")
            
            protein_logo(filepath)
            image = True
            return render(request, template_name, {'form':form, 'image':image, 'family':family, 'orf': orf, 'repname':repname})
        
    else:
        form = ENV_repname_Form()
    return render(request, template_name, {'form':form, 'family':family, 'orf':orf})

### Karyotype ###

# function for generating chromosome karyotype images
def karyotype(df):
    # Takes a pandas dataframe (df) as an argument containing information for all chromosomes 

    chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY']

    positions = []

    # for each chromosome in the list...
    for n in chromosomes:
        # find that chromosome in the dataframe
        chromosome = list(df.loc[df['genoName'] == n]['genoName'])
        # find the genomic start positions for repeats in that chromosome
        starts = list(df.loc[df['genoName'] == n]['genoStart'])
        # find the genomic end positions for repeats in that chromosome
        ends = list(df.loc[df['genoName'] == n]['genoEnd'])
        # find the strand (+/-) for repeats in that chromosome
        strand = list(df.loc[df['genoName'] == n]['strand'])
        # set up a dict for column headings
        d = {'chromosome': chromosome, 'starts': starts, 'ends': ends, 'strand':strand}
        # use pandas to make the dataframe
        dataf = pandas.DataFrame(data = d)
        # convert the pandas dataframe to an R dataframe
        r_dataframe = pandas2ri.py2ri(dataf)
        # add the R dataframe to the positions list
        positions.append(r_dataframe)

    # make a jpeg called karyotype.jpg
    ro.r.jpeg(file = 'retrotransposons/static/images/karyotype.jpg', width = 1150, height = 2000)
    # plot blank chromosomes using karyoploteR
    kp = karyoploteR.plotKaryotype(genome = "hg38")
    # for each R dataframe in the positions list
    for y in positions:
        # use GenomicRanges to get the start and end positions of repeats on each chromosome in a format karyploteR can understand
        ranges = GenomicRanges.makeGRangesFromDataFrame(y, start_field = 'starts', end_field = 'ends', starts_in_df_are_0based=True)
        # add points onto the chromosome images
        print(karyoploteR.kpPlotRegions(kp,ranges, col = "#000000"))
    ro.r('dev.off()')

# functions for processing info from database for each orf in LINE_1 and HERV into karyotype images   
def LINE1_karyotype(request):
    template_name = "retrotransposons/karyotype.html"
    family = 'LINE1'
    if request.method == 'POST':
        form = LINE1_karyotype_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname'] # repeat name chosen by the user
            
            # values list queryset to get a list of the information required by the karyotype() function (repeat name, start, end, chromosome and strand)
            repname_list = list(LINE_1.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "genoName","strand"))
            
            # turn info from queryset into a list of lists
            df_list = []
            for entry in repname_list:
                df_list.append(entry)
            df = pandas.DataFrame(data = df_list) # make a pandas dataframe from these lists
            df.columns=["repName", "genoStart", "genoEnd", "genoName","strand"] # specify the names of the columns

            karyotype(df) # accepts the pandas dataframe as its argument
            
            image = True # tell the page to display the image once it has been generated
            
            return render(request, template_name, {'form':form, 'image':image, 'family':family})
        
    else:
        form = LINE1_karyotype_Form()
    return render(request, template_name, {'form':form, 'family': family})

def HERV_karyotype(request):
    # as LINE1_karyotype(), but uses the HERV model instead

    family = 'HERV'
    template_name = "retrotransposons/karyotype.html"
    if request.method == 'POST':
        form = HERV_karyotype_Form(request.POST)
        if form.is_valid():
            repname = form.cleaned_data['repname']
            repname_list = list(HERV.objects.filter(repName = str(repname)).values_list("repName", "genoStart", "genoEnd", "genoName", "strand"))
            
            df_list = []
            for entry in repname_list:
                df_list.append(entry)
            df = pandas.DataFrame(data = df_list)
            df.columns=["repName", "genoStart", "genoEnd", "genoName", "strand"]

            karyotype(df)
            image = True
            return render(request, template_name, {'form':form, 'image':image, 'family': family})
        
    else:
        form = HERV_karyotype_Form()
    return render(request, template_name, {'form':form, 'family': family})

### DNA Sequences ###
# functions for displaying DNA sequences from LINE_1 and HERV databases
def LINE1_sequences(request):
    family = 'LINE1'
    template_name = "retrotransposons/sequences.html"
    if request.method == 'POST':
        
        form = LINE1_sequences_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname'] # get the repeat name the user chose from the dropdown list
            id_num = form.cleaned_data['id_num'] # get the id number the user entered into the form
            
            if repname == 'Select All': # call up everything if 'select all' was chosen
                info = LINE_1.objects.all()
            else:
                info = LINE_1.objects.filter(Q(repName = str(repname)) | Q(id = id_num)) # otherwise use the repeat name or ID

            filepath = "retrotransposons/static/sequences.fasta"

            # write the DNA sequences in the queryset into a fasta file that the user can download
            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+";"+str(entry.genoStart)+"-"+str(entry.genoEnd)+";"+str(entry.strand)+"\n"+str(entry.DNAseq)+"\n")
            
            form = LINE1_sequences_Form()

            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname, 'id_num':id_num})

    else:
        form = LINE1_sequences_Form()
    return render(request, template_name, {'form':form,'family':family})

def HERV_sequences(request):
    # same as LINE1_sequences, but generates a queryset from the HERV model instead

    family = 'HERV'
    template_name = "retrotransposons/sequences.html"
    if request.method == 'POST':
        
        form = HERV_sequences_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname']
            id_num = form.cleaned_data['id_num']
            
            if repname == 'Select All':
                info = HERV.objects.all()
            else:
                info = HERV.objects.filter(Q(repName = str(repname)) | Q(id = id_num))

            filepath = "retrotransposons/static/sequences.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+";"+str(entry.genoStart)+"-"+str(entry.genoEnd)+";"+str(entry.strand)+"\n"+str(entry.DNAseq)+"\n")
            
            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname})
        
    else:
        form = HERV_sequences_Form()
    return render(request, template_name, {'form':form,'family':family})


### look up AA sequence ###
def LINE1_AA_search(request):
    family = 'LINE1'
    if request.method == 'POST':
        
        form = LINE_1_AA_search_Form(request.POST)
        if form.is_valid():
            
            pep_seq = form.cleaned_data['pep_seq'] # get the amino acid sequence

            # generate a queryset from the amino acid sequence entered, looking for open reading frames containing that sequence
            info = LINE_1.objects.filter(Q(ORF0__icontains=pep_seq) | Q(ORF1__icontains=pep_seq) | Q(ORF2__icontains=pep_seq))

            if info.exists() == False: # indicate if no matches were found
                matches = 0
            else:
                matches = info.count() # otherwise count the number of matches in the queryset
         
            return render(request, 'retrotransposons/AA_search.html', {'form':form,'info':info, 'family':family, 'matches':matches})
    
    else:
        form = LINE_1_AA_search_Form()
    return render(request, 'retrotransposons/AA_search.html', {'form':form, 'family':family})

def HERV_AA_search(request):
    # as LINE_1_AA_search, but looks for the user's amino acid sequence in the HERV model

    family = 'HERV'
    if request.method == 'POST':
        
        form = HERV_AA_search_Form(request.POST)
        if form.is_valid():
            
            pep_seq = form.cleaned_data['pep_seq']

            info = HERV.objects.filter(Q(GAG__icontains=pep_seq) | Q(POL__icontains=pep_seq) | Q(ENV__icontains=pep_seq))

            if info.exists() == False: 
                matches = 0
            else:
                matches = info.count()
         
            return render(request, 'retrotransposons/AA_search.html', {'form':form,'info':info, 'family':family, 'matches':matches})
    
    else:
        form = HERV_AA_search_Form()
    return render(request, 'retrotransposons/AA_search.html', {'form':form, 'family':family})


### Peptide Sequences ### 
# functions for displaying amino acid sequences for orfs in LINE_1 and HERV databases
def ORF0_sequences(request):
    family = 'LINE1'
    orf = 'ORF0'
    template_name = "retrotransposons/ORF_sequences.html"
    if request.method == 'POST':
        
        form = ORF0_sequences_Form(request.POST) # use a for with a dropdown specific to the open reading frame
        if form.is_valid():
            
            repname = form.cleaned_data['repname'] # get the repeat name the user chose from the dropdown
            
            if repname == 'Select All':
                info = LINE_1.objects.all().exclude(ORF0='None') # include everything if 'select all' is chosen 
            else:
                info = LINE_1.objects.filter(repName = str(repname)).exclude(ORF0="None") # otherwise use the repeat name

            filepath = "retrotransposons/static/sequences.fasta"

            # write the amino acid sequences in the queryset into a fasta file that the user can download
            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+"-"+"ORF0"+";"+str(entry.strand)+"\n"+str(entry.ORF0)+"\n")
            
            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname, 'orf':orf})
        
    else:
        form = ORF0_sequences_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

def ORF1_sequences(request):
    # as ORF0_sequences, but looks for ORF1 sequences

    family = 'LINE1'
    orf = 'ORF1'
    template_name = "retrotransposons/ORF_sequences.html"
    if request.method == 'POST':
        
        form = ORF1_sequences_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname']
            
            if repname == 'Select All':
                info = LINE_1.objects.all().exclude(ORF1='None')
            else:
                info = LINE_1.objects.filter(repName = str(repname)).exclude(ORF1="None")

            filepath = "retrotransposons/static/sequences.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+"-"+"ORF1"+";"+str(entry.strand)+"\n"+str(entry.ORF1)+"\n")
            
            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname, 'orf':orf})
        
    else:
        form = ORF1_sequences_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

def ORF2_sequences(request):
     # as ORF0_sequences, but looks for ORF2 sequences

    family = 'LINE1'
    orf = 'ORF2'
    template_name = "retrotransposons/ORF_sequences.html"
    if request.method == 'POST':
        
        form = ORF2_sequences_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname']
            
            if repname == 'Select All':
                info = LINE_1.objects.all().exclude(ORF2='None')
            else:
                info = LINE_1.objects.filter(repName = str(repname)).exclude(ORF2="None")

            filepath = "retrotransposons/static/sequences.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+"-"+"ORF2"+";"+str(entry.strand)+"\n"+str(entry.ORF2)+"\n")
            
            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname, 'orf':orf})
        
    else:
        form = ORF2_sequences_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

def GAG_sequences(request):
    # as ORF0_sequences, but looks for GAG sequences in the HERV model

    family = 'HERV'
    orf = 'GAG'
    template_name = "retrotransposons/ORF_sequences.html"
    if request.method == 'POST':
        
        form = GAG_sequences_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname']
            
            if repname == 'Select All':
                info = HERV.objects.all().exclude(GAG='None')
            else:
                info = HERV.objects.filter(repName = str(repname)).exclude(GAG="None")

            filepath = "retrotransposons/static/sequences.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+"-"+"GAG"+";"+str(entry.strand)+"\n"+str(entry.GAG)+"\n")
            
            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname, 'orf':orf})
        
    else:
        form = GAG_sequences_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

def POL_sequences(request):
    # as ORF0_sequences, but looks for POL sequences in the HERV model

    family = 'HERV'
    orf = 'POL'
    template_name = "retrotransposons/ORF_sequences.html"
    if request.method == 'POST':
        
        form = POL_sequences_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname']
            
            if repname == 'Select All':
                info = HERV.objects.all().exclude(POL='None')
            else:
                info = HERV.objects.filter(repName = str(repname)).exclude(POL="None")

            filepath = "retrotransposons/static/sequences.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+"-"+"POL"+";"+str(entry.strand)+"\n"+str(entry.POL)+"\n")
            
            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname, 'orf':orf})
        
    else:
        form = POL_sequences_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

def ENV_sequences(request):
    # as ORF0_sequences, but looks for ENV sequences in the HERV model

    family = 'HERV'
    orf = 'ENV'
    template_name = "retrotransposons/ORF_sequences.html"
    if request.method == 'POST':
        
        form = ENV_sequences_Form(request.POST)
        if form.is_valid():
            
            repname = form.cleaned_data['repname']

            if repname == 'Select All':
                info = HERV.objects.all().exclude(ENV='None')
            else:
                info = HERV.objects.filter(repName = str(repname)).exclude(ENV="None")

            filepath = "retrotransposons/static/sequences.fasta"

            with open(filepath, "w") as file:
                for entry in info:
                    file.write(">"+str(entry.repName)+"-"+"ENV"+";"+str(entry.strand)+"\n"+str(entry.ENV)+"\n")
            
            return render(request, template_name, {'form':form, 'info':info, 'family':family, 'repname':repname, 'orf':orf})
        
    else:
        form = ENV_sequences_Form()
    return render(request, template_name, {'form':form,'family':family, 'orf':orf})

### Add to database ###
# functions for adding new entries to LINE_1 and HERV databases
def new_LINE1_entry(request):
    family = 'LINE1'
    template_name = "retrotransposons/new_entry.html"

    if request.method == 'POST':
        form = LINE1_Entry_Form(request.POST)
        if form.is_valid():
            
            
            # fields to produce the new entry from, taken from the form
            repName = form.cleaned_data['repName']
            repClass = form.cleaned_data['repClass']
            repFamily = form.cleaned_data['repFamily']
            genoName = form.cleaned_data['genoName']
            genoStart = form.cleaned_data['genoStart']
            genoEnd = form.cleaned_data['genoEnd']
            strand = form.cleaned_data['strand']
            DNAseq = form.cleaned_data['DNAseq']

            repStart = form.cleaned_data['repStart']
            repEnd = form.cleaned_data['repEnd']
            repLeft = form.cleaned_data['repLeft']
            swScore = form.cleaned_data['swScore']
            milliDiv = form.cleaned_data['milliDiv']
            milliDel = form.cleaned_data['milliDel']
            milliIns = form.cleaned_data['milliIns']
            genoLeft = form.cleaned_data['genoLeft']
            
            # overwrite blank entries in open reading frame fields with 'None' to be consistent with data aready in the database
            if form.cleaned_data['ORF0'] == '':
                ORF0_seq = 'None'
            else:
                ORF0_seq = form.cleaned_data['ORF0']
            if form.cleaned_data['ORF1'] == '':
                ORF1_seq = 'None'
            else:
                ORF1_seq = form.cleaned_data['ORF1']
            if form.cleaned_data['ORF2'] == '':
                ORF2_seq = 'None'
            else:
                ORF2_seq = form.cleaned_data['ORF2']

            # create the new entry in the database
            LINE_1.objects.create(
                swScore = swScore,      
                milliDiv = milliDiv, 
                milliDel = milliDel, 
                milliIns = milliIns, 
                genoName = genoName, 
                genoStart = genoStart, 
                genoEnd = genoEnd, 
                genoLeft = genoLeft, 
                strand = strand, 
                repName = repName, 
                repClass = repClass, 
                repFamily = repFamily, 
                repStart = repStart, 
                repEnd = repEnd, 
                repLeft = repLeft,
                DNAseq = DNAseq,
                ORF0 = ORF0_seq,
                ORF1 = ORF1_seq,
                ORF2 = ORF2_seq
                )
            
            # check the new entry was added, should be the last item. Will be used to display the ID of the new entry
            new_entry = LINE_1.objects.last()
            print(new_entry)
            
            return render_to_response("retrotransposons/success.html",{'family':family, 'new_entry':new_entry})
    
    else:
        form = LINE1_Entry_Form()
    return render(request, template_name, {'form':form,'family':family})

def new_HERV_entry(request):
    # add new_LINE1_entry, but adds a new entry to the HERV model (GAG,POL,ENV instead of ORF0,ORF1,ORF2)

    family = 'HERV'
    template_name = "retrotransposons/new_entry.html"

    if request.method == 'POST':  
        form = New_HERV_Entry_Form(request.POST)
        if form.is_valid():

            # fields from the form to get information for the new entry
            repName = forms.cleaned_data['repName']
            repClass = forms.cleaned_data['repClass']
            repFamily = forms.cleaned_data['repFamily']
            genoName = forms.cleaned_data['genoName']
            genoStart = forms.cleaned_data['genoStart']
            genoEnd = forms.cleaned_data['genoEnd']
            strand = forms.cleaned_data['strand']
            DNAseq = forms.cleaned_data['DNAseq']

            swScore = forms.cleaned_data['swScore']
            milliDiv = forms.cleaned_data['milliDiv']
            milliDel = forms.cleaned_data['milliDel']
            milliIns = forms.cleaned_data['milliIns']
            genoLeft = forms.cleaned_data['genoLeft']
            
            
            # replace blank strings with 'None' to be consistent with data already in the model
            if form.cleaned_data['GAG'] == '':
                GAG_seq = 'None'
            else:
                GAG_seq = form.cleaned_data['GAG']
            if form.cleaned_data['POL'] == '':
                POL_seq = 'None'
            else:
                POL_seq = form.cleaned_data['POL']
            if form.cleaned_data['ENV'] == '':
                ENV_seq = 'None'
            else:
                ENV_seq = form.cleaned_data['ENV']

            HERV.objects.create(
                swScore = swScore,      
                milliDiv = milliDiv, 
                milliDel = milliDel, 
                milliIns = milliIns, 
                genoName = genoName, 
                genoStart = genoStart, 
                genoEnd = genoEnd, 
                genoLeft = genoLeft, 
                strand = strand, 
                repName = repName, 
                repClass = repClass, 
                repFamily = repFamily, 
                repStart = repStart, 
                repEnd = repEnd, 
                repLeft = repLeft,
                DNAseq = DNAseq,
                GAG = GAG_seq,
                POL = POL_seq,
                ENV = ENV_seq
                )
            
            new_entry = HERV.objects.last()
            print(new_entry)
            
            return render_to_response("retrotransposons/success.html",{'family':family, 'new_entry':new_entry})

    else:
        form = New_HERV_Entry_Form()
    return render(request, template_name, {'form':form,'family':family})

def new_Atlas_entry(request):
    # similar to the other two new entry functions, but uses form.save()

    family = 'Expression Atlas'
    template_name = "retrotransposons/new_entry.html"

    if request.method == 'POST':
        
        form = Atlas_Form(request.POST)
        
        if form.is_valid():
            form.save() # since no fields need to be changed ("" > "None"), the form.save() method is used to easily add a new entry to the model

            new_entry = Atlas.objects.last()
            return render(request, "retrotransposons/success.html",{'family':family, 'new_entry':new_entry})

    else:
        form = Atlas_Form()
    return render(request, template_name, {'form':form,'family':family})

### info pages ###
# functions for generating graphs used in information pages
def LINE1_info(request):
    family = 'LINE1'
    # generate the chart graphics used on the page. These images are generated each time the page is loaded.
    # new info in the database will change the images to reflect the changes
    stacked_plot_chr(family)
    stacked_plot_repname(family)
    bar_plot_chr(family)
    bar_plot_repname(family)

    template_name = "retrotransposons/LINE1_info.html" 

    return render(request, template_name)

def HERV_info(request):
    # as LINE1_info, but displays graphics for the HERV model by changing the 'family' variabl to 'HERV'
    family = 'HERV'
    stacked_plot_chr(family)
    stacked_plot_repname(family)
    bar_plot_chr(family)
    bar_plot_repname(family)

    template_name = "retrotransposons/HERV_info.html" 

    return render(request, template_name)  
   
'''
# remove ''' from this file when instructed!

