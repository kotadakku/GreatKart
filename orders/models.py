from django.db import models

from accounts.models import Account
from store.models import Product, Variation

class Payment(models.Model):
    class Meta:
        verbose_name = "Thanh toán"
        verbose_name_plural = "Thanh toán"
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name="Người dùng")
    payment_id = models.CharField(max_length=100,verbose_name="Mã thanh toán")
    payment_method = models.CharField(max_length=100,verbose_name="Phương thức thanh toán")
    amount_paid = models.CharField(max_length=100,verbose_name="Tiền trả")
    status = models.CharField(max_length=100,verbose_name="Trạng thái")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Tạo ra")

    def __str__(self):
        return self.payment_id


class Order(models.Model):
    class Meta:
        verbose_name = "Đặt hàng"
        verbose_name_plural = "Đặt hàng"
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,verbose_name="Người dùng")
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Thanh toán")
    order_number = models.CharField(max_length=20,verbose_name="Mã đơn hàng")
    first_name = models.CharField(max_length=50,verbose_name="Họ")
    last_name = models.CharField(max_length=50,verbose_name="Tên")
    phone = models.CharField(max_length=15,verbose_name="SĐT")
    email = models.EmailField(max_length=50,verbose_name="Email")
    address_line_1 = models.CharField(max_length=50,verbose_name="Địa chỉ đặt hàng")
    address_line_2 = models.CharField(max_length=50, blank=True,verbose_name="Địa chỉ giao hàng")
    country = models.CharField(max_length=50,verbose_name="Quốc gia")
    state = models.CharField(max_length=50,verbose_name="Huyện")
    city = models.CharField(max_length=50,verbose_name="Thành phố")
    order_note = models.CharField(max_length=100, blank=True,verbose_name="Ghi chú")
    order_total = models.FloatField(verbose_name="Tổng đơn hàng")
    tax = models.FloatField(verbose_name="Thuế")
    status = models.CharField(max_length=10, choices=STATUS, default='New',verbose_name="Trạng thái")
    ip = models.CharField(blank=True, max_length=20,verbose_name="Mã")
    is_ordered = models.BooleanField(default=False,verbose_name="Tình trạng hàng")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Ngày kết thúc")

    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def full_address(self):
        return "{0} {1}".format(self.address_line_1, self.address_line_2)

    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    class Meta:
        verbose_name = "Đặt sản phẩm"
        verbose_name_plural = "Đặt sản phẩm"
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name="Đặt hàng")
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Thanh toán")
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name="Người dùng")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Sản phẩm")
    variations = models.ManyToManyField(Variation, blank=True,verbose_name="Loại")
    quantity = models.IntegerField(verbose_name="Số lượng")
    product_price = models.FloatField(verbose_name="Giá sản phẩm")
    ordered = models.BooleanField(default=False,verbose_name="Đã đặt hàng")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Ngày giao")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Ngày kết thúc")

    def __str__(self):
        return self.product.product_name
