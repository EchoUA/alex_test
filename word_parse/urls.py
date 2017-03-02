from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'word_parse'

urlpatterns = [

    url(r'^simple/', views.get_text, name='simpe'),

]
