from django.shortcuts import render
from rest_framework import viewsets

from service.models import UrunFiyat, UrunOzellikleri, IlceModel, SehirModel, KategoriModel, AltKategoriModel, \
    UrunModel, UrunResimler
from service.serializers import UrunFiyatSerializer, UrunOzellikleriSerializer, IlceSerializer, SehirSerializer, \
    KategoriSerializer, AltKategoriSerializer, UrunSerializer, UrunResimlerSerializer


class IlceViewSet(viewsets.ModelViewSet):
    queryset = IlceModel.objects.all()
    serializer_class = IlceSerializer


class SehirViewSet(viewsets.ModelViewSet):
    queryset = SehirModel.objects.all()
    serializer_class = SehirSerializer


class KategoriViewSet(viewsets.ModelViewSet):
    queryset = KategoriModel.objects.all()
    serializer_class = KategoriSerializer


class AltKategoriViewSet(viewsets.ModelViewSet):
    queryset = AltKategoriModel.objects.all()
    serializer_class = AltKategoriSerializer



class UrunViewSet(viewsets.ModelViewSet):
    queryset = UrunModel.objects.all()
    serializer_class = UrunSerializer


class UrunResimlerViewSet(viewsets.ModelViewSet):
    queryset = UrunResimler.objects.all()
    serializer_class = UrunResimlerSerializer


class UrunOzellikleriViewSet(viewsets.ModelViewSet):
    queryset = UrunOzellikleri.objects.all()
    serializer_class = UrunOzellikleriSerializer


class UrunFiyatViewSet(viewsets.ModelViewSet):
    queryset = UrunFiyat.objects.all()
    serializer_class = UrunFiyatSerializer

"""
class KampanyaViewSet(viewsets.ModelViewSet):
    queryset = KampanyaModel.objects.all()
    serializer_class = KampanyaSerializer


class KampanyaUrunViewSet(viewsets.ModelViewSet):
    queryset = KampanayaUrun.objects.all()
    serializer_class = KampanyaUrunSerializer
    

class KargoViewSet(viewsets.ModelViewSet):
    queryset = KargoModel.objects.all()
    serializer_class = KargoSerializer

"""