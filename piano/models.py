from django.db import models


# Create your models here.

class Piano(models.Model):
    artist = models.CharField('艺术家', max_length=60)

    class Meta:
        db_table = 'piano'
