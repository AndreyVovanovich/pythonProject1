from django.db import models

# Create your models here.
from django.db import models
class SearchingUsers(models.Model):

    ByName = models.CharField(max_length=100)
