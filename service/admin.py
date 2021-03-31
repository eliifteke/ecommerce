from django.contrib import admin

from service.models import SehirModel, IlceModel, KategoriModel, AltKategoriModel, UrunModel, UrunOzellikleri, \
    UrunResimler, UrunFiyat

admin.site.register(SehirModel)
admin.site.register(IlceModel)
admin.site.register(KategoriModel)
admin.site.register(AltKategoriModel)
admin.site.register(UrunModel)
admin.site.register(UrunResimler)
admin.site.register(UrunOzellikleri)
admin.site.register(UrunFiyat)


