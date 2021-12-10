from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.


class Product(models.Model):
    name = CharField(max_length=259, null=False, blank=False)
    composition = TextField()
    benefits = TextField()
    dossage = TextField()
    package = CharField(max_length=259)

    def __str__(self) -> str:
        return self.name
