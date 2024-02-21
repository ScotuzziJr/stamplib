from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name


class Stamp(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=350, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self) -> str:
        return {"Stamp": self.name, "Description": self.description}
