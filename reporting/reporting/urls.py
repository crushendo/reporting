from django.conf.urls import include, url
from django.contrib import admin
from scoutapp import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login), 
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout), 
    url(r'^accounts/loggedin/$', views.loggedin), 
    url(r'^accounts/invalid/$', views.invalid_login), 
    url(r'^labelle/wps$', TemplateView.as_view(template_name='labelle/wps.html'), name='wps'), 
    url(r'^report$', views.report,name='report'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'), 
    url(r'^labelle/scouting/mature$', views.labelleMature,name='mature'),
    url(r'^labelle/scouting/young$', views.labelleYoung,name='young'),
    url(r'^labelle/scouting/mature_form$', views.labelleMatureForm,name='mature_form'),
    url(r'^labelle/scouting/young_form$', views.labelleYoungForm,name='young_form'),
    url(r'^labelle/spray_input$', views.sprayInput, name='spray_input'),
    url(r'^spray_report$', views.sprayReport,name='spray_report'),
    url(r'^labelle/leaf_input$', views.leafInput, name='leaf_input'),
    url(r'^labelle/leaf_remove$', views.leafRemove, name='leaf_remove'),
    url(r'^labelle/leaf_check$', views.leafCheck, name='leaf_check'),
    url(r'^leaf_report$', views.leafReport, name='leaf_report'),
    url(r'^manage$', views.manage,name='manage'),
    url(r'^manage_labelle/leaf_samples$', views.labelle_leaf_samples,name='leaf_samples'),
    url(r'^manage_labelle/leaf_samples_add_field$', views.labelle_leaf_samples_add_field,name='leaf_samples_add_field'),
    url(r'^manage_labelle/leaf_samples_edit_field$', views.labelle_leaf_samples_edit_field,name='leaf_samples_edit_field'),
    url(r'^manage_labelle/leaf_samples_add_nutrient$', views.labelle_leaf_samples_add_nutrient,name='leaf_samples_add_nutrient'),
    url(r'^manage_labelle/leaf_samples_edit_nutrient$', views.labelle_leaf_samples_edit_nutrient,name='leaf_samples_edit_nutrient'),
    url(r'^labelle/scouting/rust_mites$', views.rustMites, name='rust_mites'),
    url(r'^rust_mite_report$', views.rustMiteReport,name='rust_mite_report'),    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
