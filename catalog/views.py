from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def products_lict(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def product_detail(reqest, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(reqest, "product_detail.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name} Телефон: {phone}, Ваше сообщение получено<br>Сообщение: {message}"
        )
    return render(request, "contacts.html")
