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

class UrunResmiSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrunModel
        fields = ['resim']

class UrunResimlerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrunResimler
        fields = '__all__'

class UrunFiyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrunFiyat
        fields = '__all__'

class UrunSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrunModel
        fields = '__all__'



class UrunDetailSerializer(serializers.ModelSerializer):
    urun=UrunSerializer()
    class Meta:
        model = UrunResimler
        fields = ['urun', 'urunresim', 'sliderresim']




class UrunOzellikleriSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrunOzellikleri
        fields = '__all__'


class ResimListSerializer(serializers.Serializer):
    urun = serializers.RelatedField(source='urun', read_only=True)
    urunresim = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False)
    )
    sliderresim = serializers.BooleanField()
    def create(self, validated_data):
        urun = validated_data.pop('urun')
        urunresim = validated_data.pop('urunresim')
        sliderresim = validated_data.pop('sliderresim')

        for file in urunresim:
            f = UrunResimler.objects.create(urun=urun, urunresim=file,sliderresim=sliderresim)
        return f

