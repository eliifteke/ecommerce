# Generated by Django 3.1.7 on 2021-05-14 21:51

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import service.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategoriModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('adi', models.CharField(max_length=255, verbose_name='Adi')),
            ],
            options={
                'verbose_name': 'AltKategoriler',
                'verbose_name_plural': 'AltKategoriler',
                'db_table': 'altkategoritb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='KategoriModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('adi', models.CharField(max_length=255, verbose_name='Adi')),
                ('kdvorani', models.IntegerField(default=18, verbose_name='Kdv Orani ')),
                ('slug', models.SlugField(default='', editable=False, max_length=255, verbose_name='Slug')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kategoriler',
                'verbose_name_plural': 'Kategoriler',
                'db_table': 'kategoritb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='UrunModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('adi', models.CharField(max_length=255, verbose_name='Ürün Adi ')),
                ('aciklama', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ürün Açıklama ')),
                ('aktifmi', models.BooleanField(default=False, verbose_name='Ürün Aktif Mi ')),
                ('stok', models.IntegerField(default=1, verbose_name='Stok ')),
                ('slug', models.SlugField(default='', editable=False, verbose_name='Ürün Slug')),
                ('altkategoriId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.altkategorimodel', verbose_name='Alt Kategori')),
                ('kategoriId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.kategorimodel', verbose_name='Kategori')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ürün Modeli',
                'verbose_name_plural': 'Ürün Modeli',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='UrunResimler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('urunresim', models.ImageField(upload_to=service.models.file_urun_save, verbose_name='Ürün Resim ')),
                ('sliderresim', models.BooleanField(default=False, verbose_name='Sliderde Gösterilsin Mi ')),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.urunmodel', verbose_name='Ürün ')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ürün Galerisi',
                'verbose_name_plural': 'Ürün Galerisi',
                'db_table': 'urunresimtb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='UrunOzellikleri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('aciklama', ckeditor.fields.RichTextField(verbose_name='Açıklama ')),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.urunmodel', verbose_name='Ürün')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ürün Özellik ',
                'verbose_name_plural': 'Ürün Özellik ',
                'db_table': 'urunozelliktb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='UrunFiyat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('satisfiyati', models.FloatField(default=0, verbose_name='Satiş Fiyati ')),
                ('urun', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='service.urunmodel', verbose_name='Ürün')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ürün Fiyatı ',
                'verbose_name_plural': 'Ürün Fiyatı',
                'db_table': 'urunfiyattb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='SehirModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('adi', models.CharField(max_length=255, verbose_name='Adi')),
                ('aktifmi', models.BooleanField(default=True, verbose_name='Aktif Mi')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Şehir',
                'verbose_name_plural': 'Şehir',
                'db_table': 'sehirtb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='IlceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('adi', models.CharField(max_length=255, verbose_name='Adi')),
                ('aktifmi', models.BooleanField(default=True, verbose_name='Aktif Mi')),
                ('sehir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.sehirmodel', verbose_name='Şehir')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'İlçe',
                'verbose_name_plural': 'İlçe',
                'db_table': 'ilcetb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.AddField(
            model_name='altkategorimodel',
            name='kategoriId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.kategorimodel', verbose_name='Kategori'),
        ),
        migrations.AddField(
            model_name='altkategorimodel',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AdresModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('adres', models.CharField(max_length=255, verbose_name='Adres')),
                ('yedekTelefon', models.CharField(max_length=255, verbose_name='Telefon')),
                ('ilce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ilcemodel', verbose_name='Ilce')),
                ('sehir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.sehirmodel', verbose_name='Şehir')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Adres',
                'verbose_name_plural': 'Adres',
                'db_table': 'adrestb',
                'ordering': ['-create_at'],
            },
        ),
    ]
