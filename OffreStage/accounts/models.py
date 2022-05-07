from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from django.contrib.auth.models import AbstractUser

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("L'email est obligatoire")
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        user=self.create_user(email=self.normalize_email(email),password=password)
        user.account_type="admin"
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
class Utilisateur(AbstractUser):
    email=models.EmailField(max_length=60,unique=True)
    date_joined=models.DateTimeField(auto_now=True)
    account_type=models.CharField(max_length=10,default="student")
    phone_number=models.CharField(max_length=10, blank=True)
    address=models.CharField(max_length=500,blank=True)
    birthday=models.DateField(null=True)
    photo=models.ImageField(null=True,blank=True)
    Cv=models.FileField(upload_to ='media/',null=True,blank=True)
    nom_entreprise=models.CharField(max_length=50,null=True,blank=True)
    domaine=models.CharField(max_length=50,null=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=UserManager()
    def __str__(self):
        return self.email
    def has_perm(self, perm: str, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True