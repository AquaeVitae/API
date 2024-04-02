"""
URL configuration for aquaevitae_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from partnerships import urls as partnerships_urls
from recommendations import urls as recommendations_urls
from products import urls as products_urls
from analysis import urls as analysis_urls


admin.site.disable_action("delete_selected")
admin.site.site_url = "../v1/swagger"
admin.site.site_header = "Aquaevitae manager"
admin.autodiscover()

schema_view = get_schema_view(
    openapi.Info(title="Aquaevitae API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

v1_urlpatterns = (
    [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]
    + recommendations_urls.urlpatterns
    + products_urls.urlpatterns
    + partnerships_urls.urlpatterns
    + analysis_urls.urlpatterns
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include((v1_urlpatterns, "v1"), namespace="v1")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
