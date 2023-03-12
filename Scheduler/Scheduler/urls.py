"""Scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from app_calendar import views as cal_views
from django.views.generic import TemplateView

# router = DefaultRouter()
# router.register('books', cal_views.BooksViewSet)

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Dummy API",
        default_version='v1',
        description="Dummy description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@dummy.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', cal_views.index),
    # path('', include(router.urls)),
    # path('login/', cal_views.login),
    path('calendar/', cal_views.cal_main),
    path('user/', cal_views.user),
    path('api/', include('app_calendar.urls')),
    path(r'docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# path('swagger-ui/', TemplateView.as_view(
#         template_name='swagger-ui.html',
#         extra_context={'schema_url':'openapi-schema'}
#     ), name='swagger-ui')
