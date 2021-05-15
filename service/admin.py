from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from service.models import SehirModel, IlceModel, KategoriModel, AltKategoriModel, UrunModel, UrunOzellikleri, \
    UrunResimler, UrunFiyat, AdresModel


class UrunGaleriInline(NestedStackedInline):
    model = UrunResimler
    extra = 5

class UrunOzellikInline(NestedStackedInline):
    model = UrunOzellikleri
    extra = 5


class UrunFiyatInline(NestedStackedInline):
    model = UrunFiyat
    extra = 1


@admin.register(KategoriModel)
class AdminKategori(admin.ModelAdmin):
    list_display = ['id', 'adi', 'slug', 'kdvorani']
    search_fields = ['adi']

    class Meta:
        model = KategoriModel


@admin.register(AltKategoriModel)
class AdminAltKategori(admin.ModelAdmin):
    list_display = ['id', 'adi', 'kategoriId']
    search_fields = ['adi']

    class Meta:
        model = AltKategoriModel



@admin.register(UrunModel)
class AdminUrun(NestedModelAdmin):
    list_display = ['id', 'adi', 'slug', 'kategoriId', 'altkategoriId','aktifmi', 'stok']
    search_fields = ['adi']
    list_filter = ['kategoriId']
    list_editable = ['aktifmi']
    inlines = [UrunFiyatInline,UrunGaleriInline,UrunOzellikInline]

    class Meta:
        model = UrunModel


@admin.register(UrunResimler)
class AdminUrunResim(NestedModelAdmin):
    list_display = ['id', 'urun', 'urunresim']
    search_fields = ['urun']

    class Meta:
        model = UrunResimler

@admin.register(UrunOzellikleri)
class AdminUrunOzellik(NestedModelAdmin):
    list_display = ['id', 'urun', 'aciklama']
    search_fields = ['urun']


    class Meta:
        model = UrunOzellikleri


@admin.register(UrunFiyat)
class AdminUrunFiyat(NestedModelAdmin):
    list_display = ['id', 'urun', 'satisfiyati']
    search_fields = ['urun']

    class Meta:
        model = UrunFiyat


@admin.register(SehirModel)
class AdminSehir(ImportExportModelAdmin):
    list_display = ['id', 'adi', 'aktifmi']
    list_editable = ['aktifmi']
    search_fields = ['adi']

    class Meta:
        model = SehirModel


@admin.register(IlceModel)
class AdminIlce(ImportExportModelAdmin):
    list_display = ['id', 'adi', 'sehir', 'aktifmi']
    list_filter = ['sehir']
    search_fields = ['adi']
    list_editable = ['aktifmi']

    class Meta:
        model = IlceModel



admin.site.register(AdresModel)


