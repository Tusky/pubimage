from django.conf.urls import patterns, include, url
from django.contrib import admin
from imgupload.views import top10_list

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pubimage.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^temp/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'temp/'}),

    url(r'^login/', 'personel.views.login_view', name='login'),
    url(r'^logout/', 'personel.views.logout_view', name='logout'),
    url(r'^register/', 'personel.views.register_view', name='register'),
    url(r'^top10/', 'imgupload.views.top10_list', name='top10'),
    # USER OPTIONS
    url(r'^upload/', 'imgupload.views.upload_new_image', name='upload'),
    url(r'^manage/', 'imgupload.views.manage_images', name='manage'),
    url(r'^remove/(?P<image_id>\w+)', 'imgupload.views.remove_image', name='remove'),
    # IMAGE OPTIONS
    url(r'^image/(?P<image_id>\w+)$', 'imgupload.views.show_image', name='show_image'),
    url(r'^image/(?P<image_id>\w+)/like', 'imgupload.views.like_image', name='like_image'),
    url(r'^image/(?P<image_id>\w+)/dislike', 'imgupload.views.dislike_image', name='dislike_image'),
)
