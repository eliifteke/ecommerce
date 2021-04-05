from django.shortcuts import render
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from service.models import UrunFiyat, UrunOzellikleri, IlceModel, SehirModel, KategoriModel, AltKategoriModel, \
    UrunModel, UrunResimler,  AdresModel
from service.serializers import UrunFiyatSerializer, UrunOzellikleriSerializer, IlceSerializer, SehirSerializer, \
    KategoriSerializer, AltKategoriSerializer, UrunSerializer, UrunResimlerSerializer,  AdresSerializer


class IlceViewSet(viewsets.ModelViewSet):
    queryset = IlceModel.objects.all()
    serializer_class = IlceSerializer


class SehirViewSet(viewsets.ModelViewSet):
    queryset = SehirModel.objects.all()
    serializer_class = SehirSerializer

class AdresViewSet(viewsets.ModelViewSet):
    queryset = AdresModel.objects.all()
    serializer_class = AdresSerializer



class KategoriViewSet(viewsets.ModelViewSet):
    queryset = KategoriModel.objects.all()
    serializer_class = KategoriSerializer


class AltKategoriViewSet(FlexFieldsModelViewSet):
    queryset = AltKategoriModel.objects.all()
    serializer_class = AltKategoriSerializer


class UrunViewSet(viewsets.ModelViewSet):
    queryset = UrunModel.objects.all()
    serializer_class = UrunSerializer
    lookup_field = "slug"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["adi"]


class UrunResimlerViewSet(viewsets.ModelViewSet):
    queryset = UrunResimler.objects.all()
    serializer_class = UrunResimlerSerializer


class UrunOzellikleriViewSet(viewsets.ModelViewSet):
    queryset = UrunOzellikleri.objects.all()
    serializer_class = UrunOzellikleriSerializer


class UrunFiyatViewSet(viewsets.ModelViewSet):
    queryset = UrunFiyat.objects.all()
    serializer_class = UrunFiyatSerializer

