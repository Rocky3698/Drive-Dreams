from django.db import models
from django.utils.text import slugify
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100,unique=True)
    country = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name} {self.country}")
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name