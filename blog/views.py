from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        article.views += 1
        article.save()

        return article


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ("title", "content", "preview")

    def get_success_url(self):
        return reverse("blog:article_detail", kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article_list")
