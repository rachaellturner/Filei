
from django.contrib import admin
from django.urls import path

from django.conf.urls import url

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# get functions from views.py to be used with urls

# uncomment this when instructed!
'''from retrotransposons.views import (
    LINE1_upload_mztab_file,
    LINE1_upload_mzID_file, 
    HERV_upload_mztab_file,
    HERV_upload_mzID_file,
    simple_HERV_table,
    simple_LINE1_table,
    Atlas_table,
    ORF0_protein_logo,
    ORF1_protein_logo,
    ORF2_protein_logo,
    GAG_protein_logo,
    POL_protein_logo,
    ENV_protein_logo,
    LINE1_karyotype,
    HERV_karyotype,
    LINE1_sequences,
    HERV_sequences,
    ORF0_sequences,
    ORF1_sequences,
    ORF2_sequences,
    GAG_sequences,
    POL_sequences,
    ENV_sequences,
    new_LINE1_entry,
    new_HERV_entry,
    new_Atlas_entry,
    LINE1_info,
    HERV_info,
    LINE1_AA_search,
    HERV_AA_search
)
'''

urlpatterns = []
''' # uncomment this when instructed!   
    
    # format: url(path, function)

    # built in admin functionality
    path('admin/', admin.site.urls),
    
    # home page, no funcion, just uses template
    url(r'^home/$', TemplateView.as_view(template_name = 'home.html')),
    
    # about page
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html')),

    # contact page
    url(r'^contact/$', TemplateView.as_view(template_name = 'contact.html')),
    
    # overview page
    url(r'^overview/$', TemplateView.as_view(template_name = 'retrotransposons/overview.html')),
    
    # phylogeny page
    url(r'^LINE1_phylogeny/$', TemplateView.as_view(template_name = 'retrotransposons/LINE1_phylogeny.html')),
    url(r'^HERV_phylogeny/$', TemplateView.as_view(template_name = 'retrotransposons/HERV_phylogeny.html')),
    
    #information pages
    url(r'^LINE1_info/$', LINE1_info),
    url(r'^HERV_info/$', HERV_info),
    
    # table pages
    url(r'^HERV_Table/$', simple_HERV_table),
    url(r'^LINE1_Table/$', simple_LINE1_table),
    url(r'^Atlas_Table/$', Atlas_table),
    
    #file upload pages
    url(r'^LINE1_upload_mzTab/$', LINE1_upload_mztab_file),
    url(r'^LINE1_upload_mzID/$', LINE1_upload_mzID_file),
    url(r'^HERV_upload_mzTab/$', HERV_upload_mztab_file),
    url(r'^HERV_upload_mzID/$', HERV_upload_mzID_file),
    
    # protein logo (alignment) pages
    url(r'^ORF0_protein_logo/$', ORF0_protein_logo),
    url(r'^ORF1_protein_logo', ORF1_protein_logo),
    url(r'^ORF2_protein_logo/$', ORF2_protein_logo),
    url(r'^GAG_protein_logo/$', GAG_protein_logo),
    url(r'^POL_protein_logo/$', POL_protein_logo),
    url(r'^ENV_protein_logo/$', ENV_protein_logo),
    
    # karyotype (distribution) pages
    url(r'^LINE1_karyotype/$', LINE1_karyotype),
    url(r'^HERV_karyotype/$', HERV_karyotype),
    
    # DNA sequences pages
    url(r'^LINE1_sequences/$', LINE1_sequences),
    url(r'^HERV_sequences/$', HERV_sequences),
    
    # peptide sequences pages
    url(r'^ORF0_sequences/$', ORF0_sequences),
    url(r'^ORF1_sequences/$', ORF1_sequences),
    url(r'^ORF2_sequences/$', ORF2_sequences),
    url(r'^GAG_sequences/$', GAG_sequences),
    url(r'^POL_sequences/$', POL_sequences),
    url(r'^ENV_sequences/$', ENV_sequences),
    
    # new database entry pages
    url(r'^new_LINE1_entry/$', new_LINE1_entry),
    url(r'^new_HERV_entry/$', new_HERV_entry),
    url(r'^new_Atlas_entry/$', new_Atlas_entry),

    # AA search pages
    url(r'^LINE1_AA_search/$', LINE1_AA_search),
    url(r'^HERV_AA_search/$', HERV_AA_search)

] 
'''


# include media folder for storing documents
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





