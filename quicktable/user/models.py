from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from common.models import BaseModel

# Create your models here.

__all__ = ['QTUser', 'UserInfo']


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError("Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        
        return self.create_user(email=email, password=password, **extra_fields)
    
    def get_by_natural_key(self, email: str) -> str:
        return super().get_by_natural_key(email)
    

class QTUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=45)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    class Meta:
        db_table = 'qt_user'
        

class UserInfo(BaseModel):
    user = models.ForeignKey('user.QTUser', related_name="+", on_delete=models.CASCADE)
    username = models.CharField(null=True, max_length=45)
    first_name = models.CharField(null=True, max_length=45)
    last_name = models.CharField(null=True, max_length=45)
    phone = models.CharField(null=True, max_length=10)
    address = models.CharField(null=True, max_length=45)
    
    class Meta:
        db_table = 'qt_user_info'
    
    
    