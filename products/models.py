from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# Create your models here.
class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    
    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})

class Product(TimeStampedModel):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    is_available = models.BooleanField(default=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug", self.slug})