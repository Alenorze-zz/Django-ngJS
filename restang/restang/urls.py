from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from restang.views import RestangListView, RestangDetailView

admin.autodiscover()


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^restang/api/$', RestangListView.as_view()),
    url(r'^restang/api/(?P<pk>[0-9]+)/$', RestangDetailView.as_view())
]
