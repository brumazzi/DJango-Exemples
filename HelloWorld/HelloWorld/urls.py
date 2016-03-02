from django.conf.urls import include, url
from HelloApp.views import index, form
from django.contrib import admin

urlpatterns = [
    url(r'^$',index),
    url(r'^form/$', form),
#    url(r'^admin/', include(admin.site.urls)),
]
