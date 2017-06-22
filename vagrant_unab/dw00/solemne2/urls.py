from django.conf.urls import url
from solemne2 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalle/$', views.noticia_detalle, name='noticia_detalle'),
]