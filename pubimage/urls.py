from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pubimage.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^temp/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'temp/'}),

    url(r'^login/', 'personel.views.login_view', name='login'),
    url(r'^logout/', 'personel.views.logout_view', name='logout'),
    url(r'^register/', 'personel.views.register_view', name='register'),
    url(r'^upload/', 'imgupload.views.upload_new_image', name='upload'),
)
