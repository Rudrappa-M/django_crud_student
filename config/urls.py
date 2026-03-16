from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


def home(request):
    return HttpResponse("Django API is running successfully")


schema_view = get_schema_view(
    openapi.Info(
        title="Student CRUD API",
        default_version="v1",
        description="API documentation for student CRUD operations",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home),  # root URL added
    path('admin/', admin.site.urls),
    path("api/", include("students.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
]
