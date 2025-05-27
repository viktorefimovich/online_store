from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import products_lict

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    path("", products_lict)
]
