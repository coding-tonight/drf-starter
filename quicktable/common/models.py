from django.db import models

from app.user.models import User

# Create your models here.


class BaseModel(models.Model):
    """ Base Model
    """
    reference_id = models.UUIDField(unique=True)
    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(null=True, auto_now=False)
    
    created_by = models.ForeignKey(User, related_name='user', 
                                   db_column='created_by', on_delete=models.SET_NULL)
    
    updated_by = models.ForeignKey(User, related_name='user', 
                                   db_column='created_by', on_delete=models.SET_NULL, null=True)
    
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True