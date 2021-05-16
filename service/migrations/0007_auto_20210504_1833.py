# Generated by Django 3.1.7 on 2021-05-04 15:33

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import service.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0006_auto_20210405_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urunfiyat',
            name='urun',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='service.urunmodel', verbose_name='Ürün'),
        ),
        migrations.CreateModel(
            name='KampanyaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('baslik', models.CharField(max_length=255, verbose_name='Başlığı :')),
                ('aciklamasi', ckeditor.fields.RichTextField(verbose_name='Açıklamasi :')),
                ('gorsel', models.ImageField(upload_to=service.models.file_gorsel_save, verbose_name='Görsel')),
                ('aktifmi', models.BooleanField(default=True, verbose_name='Aktif Mi')),
                ('update_at', models.DateField(verbose_name='Bitiş Tarihi')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kampanyalar',
                'verbose_name_plural': 'Kampanyalar',
                'db_table': 'kampanyatb',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='KampanayaUrun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('baslangictarihi', models.DateTimeField(verbose_name='Başlangıç Tarihi')),
                ('bitistarihi', models.DateTimeField(verbose_name='Bitiş Tarihi')),
                ('kampanya', models.ForeignKey(limit_choices_to={'aktifmi': True}, on_delete=django.db.models.deletion.CASCADE, to='service.kampanyamodel')),
                ('urunid', models.ForeignKey(limit_choices_to={'aktifmi': True}, on_delete=django.db.models.deletion.CASCADE, to='service.urunmodel', verbose_name='Ürün')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kampanya Urun',
                'verbose_name_plural': 'Kampanya Urun',
                'db_table': 'kampanyauruntb',
                'ordering': ['-create_at'],
            },
        ),
    ]
