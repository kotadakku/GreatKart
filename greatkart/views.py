from django.shortcuts import render
from store.models import Product
from banner.models import Banner
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by("modified_date")[:16]
    banners = Banner.objects.all().filter(is_active=True)
    context = {
        'products': products,
        'banners': banners,
    }
    return render(request, 'home.html', context=context)