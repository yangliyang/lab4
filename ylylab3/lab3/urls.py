from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookmanage.views import Home,info,serch,delete,addbook,bookedit,changebook,bc,addauthor
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url('^$',Home),
	url(r'^serch',serch),
	url(r'^info/(\d*)',info),
	url(r'^delete(\d*)',delete),
	url(r'^addbook/$',addbook),
	url(r'^bookedit',bookedit),
	url(r'^changebook(\d*)',changebook),
	url(r'^bc(\d*)',bc),
	url(r'^addauthor(\d*)',addauthor),
)
