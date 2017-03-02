from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^word_parse/', include('word_parse.urls')),
    url(r'^admin/', admin.site.urls),
]