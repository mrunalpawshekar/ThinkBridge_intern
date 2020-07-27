from django.contrib import admin
from django.conf.urls import url
from converterproject.views import conversion
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('conversion', views.conversion, name='conversion'),
    url('', views.index, name='index')
]

urlpatterns += staticfiles_urlpatterns()
