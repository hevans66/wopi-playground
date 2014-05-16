from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wopiplay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^stuff/wopi/files/(?<fileid>[^/]+)$','wopiplay.wopi.views.info'),
    url(r'^stuff/wopi/files/(?<fileid>[^/]+)/contents$','wopiplay.wopi.views.contents'),
    url(r'geturl/(?<fileid>[^/]+)/','wopiplay.wopi.views.get_wopi_url')
)
