from django.db import models
from brand.models import Brand
from django.utils.text import slugify
# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='car_images/')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.brand.name} {self.model} {self.year}")
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.brand} - {self.model} ({self.year})"
