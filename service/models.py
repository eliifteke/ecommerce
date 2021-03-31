import os
from django.db import models
from ckeditor.fields import RichTextField

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    userid = models.ForeignKey('authentication.UserModel', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        abstract = True


class SehirModel(BaseModel):
    adi = models.CharField(verbose_name="Adi", max_length=255)
    aktifmi =models.BooleanField(verbose_name="Aktif Mi", default=True)

    class Meta:
        db_table = 'sehirtb'
        verbose_name = "Şehir"
        verbose_name_plural = "Şehir"
        ordering = ['-create_at']

    def __str__(self):
        return self.adi

class IlceModel(BaseModel):
    sehir = models.ForeignKey(SehirModel, on_delete=models.CASCADE , verbose_name="Şehir")
    adi = models.CharField(verbose_name="Adi", max_length=255)
    aktifmi =models.BooleanField(verbose_name="Aktif Mi", default=True)

    class Meta:
        db_table = 'ilcetb'
        verbose_name = "İlçe"
        verbose_name_plural = "İlçe"
        ordering = ['-create_at']

    def __str__(self):
        return self.adi

class KargoModel(BaseModel):
    adi = models.CharField(verbose_name="Adi" , max_length=255 )
    telefon = models.CharField(verbose_name="Telefon",max_length=255)
    aciklama = RichTextField(verbose_name="Açıklama")
    websitesi = models.CharField(verbose_name="URL " , null=True , blank=True , max_length=255)
    sirketmi = models.BooleanField(verbose_name="Şirketmi" , default=False)
    class Meta:
        db_table = 'kargotb'
        verbose_name = "Kargo"
        verbose_name_plural = "Kargo"
        ordering = ['-create_at']

    def __str__(self):
        return self.adi

def file_urun_save(intence, filename):
    filename = "urun/{}/{}".format(intence.urun.kategori, intence.urun, filename)
    return os.path.join('urun', filename)



class KategoriModel(BaseModel):
    adi = models.CharField(verbose_name="Adi", max_length=255)
    kdvorani = models.IntegerField(verbose_name="Kdv Orani ", default=18)


    def __str__(self):
        return self.adi

    class Meta:
        db_table = "kategoritb"
        verbose_name = "Kategoriler"
        verbose_name_plural = "Kategoriler"
        ordering = ['-create_at']



class AltKategoriModel(BaseModel):
    kategoriId = models.ForeignKey(KategoriModel, on_delete=models.CASCADE, verbose_name="Kategori")
    adi = models.CharField(verbose_name="Adi", max_length=255)


    def __str__(self):
        return self.adi

    class Meta:
        db_table = "altkategoritb"
        verbose_name = "AltKategoriler"
        verbose_name_plural = "AltKategoriler"
        ordering = ['-create_at']


class UrunModel(BaseModel):
    kategoriId = models.ForeignKey(KategoriModel, on_delete=models.CASCADE, verbose_name="Kategori")
    altkategoriId = models.ForeignKey(AltKategoriModel, on_delete=models.CASCADE, verbose_name="Kategori")
    adi = models.CharField(verbose_name="Ürün Adi ", max_length=255)  # String
    aciklama = RichTextField(verbose_name="Ürün Açıklama ", blank=True, null=True)
    aktifmi = models.BooleanField(verbose_name="Ürün Aktif Mi ", default=False)
    stok = models.IntegerField(verbose_name="Stok ", default=1)

    class Meta:
        verbose_name = "Ürün Modeli"
        verbose_name_plural = "Ürün Modeli"
        ordering = ['-create_at']

class UrunResimler(BaseModel):
    urun = models.ForeignKey(UrunModel, on_delete=models.CASCADE, verbose_name="Ürün ")
    urunresim = models.ImageField(upload_to=file_urun_save,default="", editable=False, verbose_name="Ürün Resim ")

    class Meta:
        db_table = 'urunresimtb'
        verbose_name = "Ürün Galerisi"
        verbose_name_plural = "Ürün Galerisi"
        ordering = ['-create_at']

class UrunOzellikleri(BaseModel):
    urun = models.ForeignKey(UrunModel, on_delete=models.CASCADE, verbose_name="Ürün")
    aciklama = RichTextField(verbose_name="Açıklama ")

    class Meta:
        db_table = 'urunozelliktb'
        verbose_name = "Ürün Özellik "
        verbose_name_plural = "Ürün Özellik "
        ordering = ['-create_at']

class UrunFiyat(BaseModel):
    urun = models.ForeignKey(UrunModel, on_delete=models.CASCADE, verbose_name="Ürün")
    satisfiyati = models.FloatField(verbose_name="Satiş Fiyati ", default=0)

    class Meta:
        db_table = 'urunfiyattb'
        verbose_name = "Ürün Fiyatı "
        verbose_name_plural = "Ürün Fiyatı"
        ordering = ['-create_at']











