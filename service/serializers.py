from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from service.models import SehirModel, IlceModel, KategoriModel, AltKategoriModel, UrunModel, UrunOzellikleri, \
    UrunFiyat, UrunResimler


class SehirSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = SehirModel
        fields = '__all__'


class IlceSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = IlceModel
        fields =('id','sehir','adi','aktifmi')
        expandable_fields = {
            'sehir': (SehirSerializer, {'many': True})
        }

class KategoriSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = KategoriModel
        fields = '__all__'

class AltKategoriSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = AltKategoriModel
        fields = ('id','kategoriId','adi')
        expandable_fields = {
            'kategoriId': (KategoriSerializer, {'many': True})
        }

class UrunSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = UrunModel
        fields = ('id','kategoriId','adi','aciklama','aktifmi','stok')
        expandable_fields = {
            'kategoriId': (KategoriSerializer, {'many': True})
        }


class UrunResimlerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = UrunResimler
        fields = ('id','urun')
        expandable_fields = {
            'urun': (UrunSerializer, {'many': True})
        }

class UrunOzellikleriSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = UrunOzellikleri
        fields = ('id','urun','aciklama')
        expandable_fields = {
            'urun': (UrunSerializer, {'many': True})
        }


class UrunFiyatSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = UrunFiyat
        fields = ('id', 'urun', 'satisfiyati')
        expandable_fields = {
            'urun': (UrunSerializer, {'many': True})
        }


"""
class KampanyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KampanyaModel
        fields = '__all__'


class KampanyaUrunSerializer(serializers.ModelSerializer):
    class Meta:
        model = KampanayaUrun
        fields = '__all__'

class KargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KargoModel
        fields = '__all__'"""