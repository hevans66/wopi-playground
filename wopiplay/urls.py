from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wopiplay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^stuff/wopi/files/test.xlsx$','wopiplay.wopi.views.info'),
    url(r'^stuff/wopi/files/test.xlsx/contents$','wopiplay.wopi.views.contents'),
    url(r'^stuff/wopi/files/test2.docx','wopiplay.wopi.views.contents')
)
