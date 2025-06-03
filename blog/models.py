from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blog/images", blank=True, null=True, verbose_name="Изображение", )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title}"
