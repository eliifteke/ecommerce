"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserViewSet, RegisterView, MyObtainTokenPairView


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from service.views import IlceViewSet, SehirViewSet, KategoriViewSet, AltKategoriViewSet, UrunViewSet, \
   UrunResimlerViewSet, UrunOzellikleriViewSet, UrunFiyatViewSet, AdresViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="E-COMMERCE API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@expenses.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'Ilce', IlceViewSet)
router.register(r'Sehir', SehirViewSet)
router.register(r'Adres', AdresViewSet)
router.register(r'Kategori', KategoriViewSet)
router.register(r'AltKategori', AltKategoriViewSet)
router.register(r'Urun', UrunViewSet)
router.register(r'UrunResimler', UrunResimlerViewSet)
router.register(r'UrunOzellikleri', UrunOzellikleriViewSet)
router.register(r'UrunFiyat', UrunFiyatViewSet)


urlpatterns = [
   path('api/', include(router.urls)),

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
