from django.db import models

# Create your models here.

class Banner(models.Model):
    description = models.TextField(verbose_name="Mô tả")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Thời gian tạo")
    images = models.ImageField(upload_to='photos/banners',verbose_name="Ảnh")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
