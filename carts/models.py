from accounts.models import Account
from django.db import models

from store.models import Product, Variation


class Cart(models.Model):
    class Meta:
        verbose_name = "Giỏ hàng"
        verbose_name_plural = "Giỏ hàng"
    cart_id = models.CharField(max_length=250, blank=True,verbose_name="Mã hàng")
    date_added = models.DateTimeField(auto_now_add=True,verbose_name="Ngày thêm")

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    class Meta:
        verbose_name = "Mã hàng"
        verbose_name_plural = "Mã hàng"
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,verbose_name="Người dùng")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Sản phẩm")
    variations = models.ManyToManyField(Variation, blank=True,verbose_name="Loại")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True,verbose_name="Giỏ hàng")
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True,verbose_name="Trạng thái")

    def sub_total(self):
        return self.quantity * self.product.price

    def __unicode__(self):
        return self.product
