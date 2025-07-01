from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Продукт",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField(verbose_name="Цена", help_text="Введите цену продукта")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца продукта", blank=True,
                              null=True, on_delete=models.CASCADE)
    checkbox = models.BooleanField(verbose_name="Признак публикации", default=False)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]
        permissions = [
            ("can_unpublish_product", "Сan unpublish product"),
            ("can_remove_product", "Сan remove product"),
        ]

    def __str__(self):
        return self.name
