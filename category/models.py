from django.db import models
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = "Loại"
        verbose_name_plural = "Loại"
    category_name = models.CharField(max_length=50, unique=True,verbose_name="Danh mục")
    slug = models.SlugField(max_length=100, unique=True,verbose_name="Loại")
    description = models.TextField(max_length=255, blank=True,verbose_name="Mô tả")
    category_image = models.ImageField(upload_to='photos/categories/', blank=True,verbose_name="Ảnh")

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
