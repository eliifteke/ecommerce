import os
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


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


class AdresModel(BaseModel):
    sehir =models.ForeignKey(SehirModel, on_delete=models.CASCADE , verbose_name="Şehir")
    ilce =models.ForeignKey(IlceModel, on_delete=models.CASCADE , verbose_name="Ilce")
    adres =models.CharField(verbose_name="Adres", max_length=255)
    yedekTelefon = models.CharField(verbose_name="Telefon",max_length=255)

    class Meta:
        db_table = 'adrestb'
        verbose_name = "Adres"
        verbose_name_plural = "Adres"
        ordering = ['-create_at']

    def __str__(self):
        return self.id

def file_urun_save(intence, filename):
    filename = "urun/{}/{}/{}/".format(intence.urun.kategoriId,intence.urun.id, filename)
    return os.path.join('urunler',str(intence.userid),filename)


class KategoriModel(BaseModel):
    adi = models.CharField(verbose_name="Adi", max_length=255)
    kdvorani = models.IntegerField(verbose_name="Kdv Orani ", default=18)
    slug = models.SlugField(verbose_name="Slug",default="", max_length=255, editable=False)


    def slugOlustur(self):
        slug = slugify(self.adi)
        unique_slug = slug
        num = 1
        while KategoriModel.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.slugOlustur()
        super(KategoriModel, self).save()

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
    altkategoriId = models.ForeignKey(AltKategoriModel, on_delete=models.CASCADE, verbose_name="Alt Kategori")
    adi = models.CharField(verbose_name="Ürün Adi ", max_length=255)  # String
    aciklama = RichTextField(verbose_name="Ürün Açıklama ", blank=True, null=True)
    fiyat = models.FloatField(verbose_name="Satiş Fiyati ", default=0)
    aktifmi = models.BooleanField(verbose_name="Ürün Aktif Mi ", default=False)
    stok = models.IntegerField(verbose_name="Stok ", default=1)
    slug = models.SlugField(verbose_name="Ürün Slug",default="", editable=False)

    def slugOlustur(self):
        slug = slugify(self.adi)
        unique_slug = slug
        num = 1
        while UrunModel.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.slugOlustur()
        super(UrunModel, self).save()


    class Meta:
        verbose_name = "Ürün Modeli"
        verbose_name_plural = "Ürün Modeli"
        ordering = ['-create_at']


class UrunResimler(BaseModel):
    urun = models.ForeignKey(UrunModel, on_delete=models.CASCADE, verbose_name="Ürün ")
    urunresim = models.FileField(upload_to=file_urun_save, verbose_name="Ürün Resim ")
    sliderresim = models.BooleanField(verbose_name="Sliderde Gösterilsin Mi " , default=False)



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

# urun -> [fiyat1 , fiyat2] => fiyat

class UrunFiyat(BaseModel):
    urun = models.OneToOneField(UrunModel, on_delete=models.CASCADE, verbose_name="Ürün")
    satisfiyati = models.FloatField(verbose_name="Satiş Fiyati ", default=0)

    class Meta:
        db_table = 'urunfiyattb'
        verbose_name = "Ürün Fiyatı "
        verbose_name_plural = "Ürün Fiyatı"
        ordering = ['-create_at']


