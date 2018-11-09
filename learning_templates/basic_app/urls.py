from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    url(r'^medative/$', views.medative, name='medative'),
    url(r'^other/$', views.other, name='other'),
]
