from rest_framework import serializers

from service.models import SehirModel, IlceModel, KategoriModel, AltKategoriModel, UrunModel, UrunOzellikleri, \
    UrunFiyat, UrunResimler,  AdresModel


class SehirSerializer(serializers.ModelSerializer):
    class Meta:
        model = SehirModel
        fields = '__all__'


class IlceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IlceModel
        fields ='__all__'


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdresModel
        fields ='__all__'

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriModel
        fields = '__all__'
        lookup_field = "slug"


class AltKategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = AltKategoriModel
        fields = '__all__'




class UrunSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrunModel
        fields = '__all__'
        lookup_field = "slug"


class UrunResimlerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrunResimler
        fields = '__all__'


class UrunOzellikleriSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrunOzellikleri
        fields = '__all__'



class UrunFiyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrunFiyat
        fields = '__all__'

