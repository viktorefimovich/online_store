from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name} Телефон: {phone}, Ваше сообщение получено<br>Сообщение: {message}"
        )
    return render(request, "contacts.html")
