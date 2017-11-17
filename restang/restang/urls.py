from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from restang.views import RestangView

admin.autodiscover()


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^restang/api/', RestangView.as_view())
]
