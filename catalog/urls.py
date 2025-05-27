from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import products_lict, product_detail

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    path("", products_lict, name="products_lict"),
    path("products/<int:pk>/", product_detail, name="product_detail"),

]
