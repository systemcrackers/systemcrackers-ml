from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static 

schema_view = get_schema_view(
   openapi.Info(
      title="locbackend",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.locbackend.com/policies/terms/",
      contact=openapi.Contact(email="contact@locbackend.local"),
      license=openapi.License(name="Locbackend License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('modelapi.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
