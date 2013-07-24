from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mmm_match.views.home', name='home'),
    # url(r'^mmm_match/', include('mmm_match.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^welcome$', 'match.views.index'), # root page
    
    url(r'^demographic$', 'match.views.demographic'), # answer demographic questions

    
    url(r'^quiz$', 'match.views.take_quiz'), # answer demographic questions
    
    )
