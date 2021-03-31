import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager):
    use_in_migaritons = True
    def _create_user(self , email , password , **extra_fields):
        if not email:
            raise ValueError('Kullanıcı Giriniz')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

def file_profil_save(intence, filename):
    filename = "kullanici/profil/{}/{}".format(intence.username, filename)
    return os.path.join('usermodul', filename)


class UserModel(AbstractUser):
    SATIS, MUSTERI, ADMIN = 0, 1, 2
    ROLES = ((SATIS, 'Satici'), (MUSTERI, 'Müşteri'), (ADMIN, 'Admin'))
    role = models.IntegerField(choices=ROLES, default=MUSTERI, verbose_name="Kullanıcı Rolu :")
    created_at = models.DateTimeField(auto_now_add=True)
    profil = models.ImageField(upload_to=file_profil_save, verbose_name="Kullanıcı Fotoğrafı", default="profil")
    dogumtarihi = models.DateField(verbose_name="Doğum Tarihi ", blank=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    is_superuser = models.BooleanField(verbose_name="Super User", default=True)


    class Meta:
        db_table = "usertb"
        verbose_name = "Kullanıcı Yönetimi"
        verbose_name_plural = "Kullanıcılar"

