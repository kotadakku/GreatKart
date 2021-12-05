from django.urls import reverse
from category.models import Category
from accounts.models import Account
from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = "Sản phẩm"
        verbose_name_plural = "Sản phẩm"
    product_name = models.CharField(max_length=200, unique=True,verbose_name="Tên sản phẩm")
    slug = models.SlugField(max_length=200, unique=True,verbose_name="Số lượng")
    description = models.TextField(max_length=500, blank=True,verbose_name="Mô tả")
    price = models.IntegerField(verbose_name="Giá")
    images = models.ImageField(upload_to='photos/products',verbose_name="Ảnh/Sản phẩm")
    stock = models.IntegerField(verbose_name="Loại")
    is_available = models.BooleanField(default=True,verbose_name="Trạng thái")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Thể loại")    # Khi xóa category thì Product bị xóa
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Thời gian tạo")
    modified_date = models.DateTimeField(auto_now=True,verbose_name="Thời gian sửa đổi")

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    class Meta:
        verbose_name = "Loại"
        verbose_name_plural = "Loại"
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Sản phẩm")
    variation_category = models.CharField(max_length=100, choices=variation_category_choice,verbose_name="Loại")
    variation_value = models.CharField(max_length=100,verbose_name="Kích thước")
    is_active = models.BooleanField(default=True,verbose_name="Trạng thái")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Thời gian tạo")

    objects = VariationManager()

    def __str__(self):
        return self.variation_value


class ReviewRating(models.Model):
    class Meta:
        verbose_name = "Loại"
        verbose_name_plural = "Viết đánh giá"
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Sản phẩm")
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name="Người dùng")
    subject = models.CharField(max_length=100, blank=True,verbose_name="Loại")
    review = models.TextField(max_length=500, blank=True,verbose_name="Đánh giá")
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True,verbose_name="Mã")
    status = models.BooleanField(default=True,verbose_name="Trạng thái")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Thời gian tạo")
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name="Thời gian kết thúc")

    def __str__(self):
        return self.subject