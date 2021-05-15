from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from authentication.models import UserModel

class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'


@admin.register(UserModel)
class AdminUserModel(UserAdmin):
    list_display = ['id', 'username', 'role', 'profil']
    class Meta:
        model = UserModel

