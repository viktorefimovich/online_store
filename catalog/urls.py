from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="products_lict"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/create", ProductCreateView.as_view(), name="product_create"),

]
