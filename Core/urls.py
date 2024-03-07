from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from Core.views import index,blog,Sitemap


app_name = 'Core'

sitemaps = {
    'sitemap': Sitemap,
}

urlpatterns = [
    path('',view=index,name='index'),
    path('/blog',view=blog,name='blog'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)