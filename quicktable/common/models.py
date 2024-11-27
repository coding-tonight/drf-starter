from django.db import models

class BaseModel(models.Model):
    """ Base Model
    """
    reference_id = models.UUIDField(unique=True)
    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(null=True, auto_now=False)
    
    created_by = models.ForeignKey('user.QTUser', related_name='+', 
                                   db_column='created_by', on_delete=models.PROTECT)
    
    updated_by = models.ForeignKey('user.QTUser', related_name='+', 
                                   db_column='updated_by', on_delete=models.PROTECT, null=True)
    
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True