from django.conf.urls import url
from . import views

# TEMPLAET TAGGING
app_name = 'basic_app'

#THE NAME IS WHAT WE ARE LOOKING FOR IN TEMPLATES!
urlpatterns = [
    url(r'^relative/$',views.relative, name = 'relative'),
    url(r'^other/$', views.other, name = 'other'),
]
