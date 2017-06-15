"""clouduniverse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from webindex.views import index as webIndex_index
from webindex.views import redirect as weIndex_redirect

# from zinnia import urls as zinnia_urls
# from django_comments import urls as django_comments_urls

# sitemaps
# from zinnia.sitemaps import TagSitemap
# from zinnia.sitemaps import EntrySitemap
# from zinnia.sitemaps import CategorySitemap
# from zinnia.sitemaps import AuthorSitemap

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', webIndex_index),
    url(r'^$', weIndex_redirect),

    # zinnia
    # url(r'^weblog/', include(zinnia_urls)),
    # url(r'^comments/', include(django_comments_urls)),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
]


# sitemaps
# sitemaps = {'tags': TagSitemap,
#             'blog': EntrySitemap,
#             'authors': AuthorSitemap,
#             'categories': CategorySitemap,}
#
# urlpatterns += [
#     include('django.contrib.sitemaps.views'),
#     url(r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
#     url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
# ]
