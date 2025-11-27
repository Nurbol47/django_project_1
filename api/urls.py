from django.conf import settings
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

from api.views import *


schema_view = get_schema_view(
    openapi.Info(
        title="Проект на Django",
        default_version="v1",
        description="Документация моего веб-приложение",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nurbolkachkynbekov47@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("car/", CarView.as_view()),
    path("person/", PersonView.as_view()),
    path("application/", ApplicationView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)