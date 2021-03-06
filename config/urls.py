"""learning_azure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='LEARNING_AZUE_APIS')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doc', schema_view),
    path('doc/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='doc'),
    # path('', include(('api_backend.apps.account.urls', 'account'), namespace='accounts')),
    path('', include(('api_backend.apps.apis.urls', 'apis'), namespace='apis')),
    path('azure_auth/', include('azure_auth.urls'))
]
